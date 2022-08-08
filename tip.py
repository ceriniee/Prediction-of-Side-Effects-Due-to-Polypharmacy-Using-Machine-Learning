from src.utils import *
from src.layers import *
import gc


# choose TIP model: 'cat' - TIP-cat
#					'add' - TIP-add
MOD = 'cat'
MAX_EPOCH = 100

# set training device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# initial model
if MOD == 'cat':
	settings = Setting(sp_rate=0.9, lr=0.01, prot_drug_dim=16, n_embed=48, n_hid1=32, n_hid2=16, num_base=32)
	model = TIP(settings, device) #settings obj와 device string
else:
	settings = Setting(sp_rate=0.9, lr=0.01, prot_drug_dim=64, n_embed=64, n_hid1=32, n_hid2=16, num_base=32)
	model = TIP(settings, device, mod='add')

# initial optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=settings.lr)

# train TIP model
for e in range(MAX_EPOCH):
	model.train() #모델을 학습모드로 전환
	optimizer.zero_grad() #한번의 Iteration이 끝나면 gradients를 0으로
	gc.collect() #garbage collect
	torch.cuda.empty_cache() #cuda cache memory 비우기
	loss = model() #model()은 model.forward()와 동일
	print(loss.item())
	loss.backward()
	optimizer.step()

# evaluate on test set
model.test()

# save trained model
torch.save(model, f'saved_model/tip-{model.mod}-example.pt')