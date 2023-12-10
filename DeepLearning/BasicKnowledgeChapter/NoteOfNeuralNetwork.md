# Neural Network
## 目录
* 感知机
	> 起源  
	> 权重  
	> 与或非门关系  
	> 多层感知机
* 神经网络
	> 神经网络的层数与感知机的关系  
	> 激活函数  
	> + 阶跃函数
	> + sigmoid
	> + ReLU函数
	> + 恒等函数
	> + softmax函数
	> + 神经网络案例手写数字识别


### 1. 感知机  

见附件2

### 2. 神经网络

Tips.1 神经网络的激活函数必须是非线性函数，使用线性函数是不存在隐藏层

Tips.2 sigmoid函数 h(x) = 1/(1+exp(-x))

Tips.3 ReLU函数 h(x) = max(0, x)

Tips.3 回归问题用恒等函数，二元分类问题用sigmoid函数，多元分类问题可以用softmax函数

Tips.4 输出层用恒等函数σ()

Tips.5 softmax函数 yk = exp(ak) / sum(exp(ai))

Tips.6 机器学习问题的步骤可以分为“学习”和“推理”两个阶段

Tips.7 MNIST数据集是由0-9数字图像构成的，训练集有6万张，测试集有1万张

Tips.8 分类问题的类别等于输出层神经元的数量

Tips.9 输入数据的集合为批

Tips.10 神经网络、深度学习与机器学习的异同点，在机器学习的基础之上更极力去避免人力的参与

Tips.11 损失函数常用均方误差和交叉误差来表示. 均方误差表达式：E=0.5*np.sum((y-t)**2); 交叉熵误差表达式：E=-np.sum(t*np.log(y+delta))

Tips.12 神经网络的学习方式是mini-batch学习方式,其中平均损失函数可表示为  
a. E=-np.sum(t*np.log(y+delta)) / batch_size  
b. 标签形式是非one-hot形式 E=-np.sum(np.log(y[np.arange(batch_size), t]+delta)) / batch_size

Tips.13 正确解为1，其他解为0是one-hot表示方式

Tips.14 不能用识别精度作为参数更新调整的指标，因为识别精度是不连续的，曲线斜率不可导，但损失函数可以

Tips.15 神经网络常用方法梯度法（梯度下降法）SGD

Tips.16 学习率这种超参数需要人工设定调整

Tips.17 学习算法SGD的实现过程：  
a. mini-batch随机选取一部分数据；  
b. 计算梯度（损失函数减小最多的方向）  
c. 权重参数沿梯度方向更新  
d. 重复以上三步骤

TIps.18 遍历随机选择的一次训练数据全集称为一次epoch,随epoch次数增加，比较训练集和测试集的精度变化判断是否存在过拟合的情况



### 3. 误差反向传播方法

Tips.1 计算图的概念，如何通过计算图计算权重参数,通过数据结构图形式表示计算流程

Tips.2 从出发到结束是正向传播，从结束点到出发点是反向传播，可用于导数计算，通过局部计算将复杂计算流程单独分成多个局部计算的简单结果

Tips.3 结合复杂函数求链式法则计算反向传播的结果

Tips.4 通过foward()和backward()实现正向和反向传播的简单层实现

Tips.5 通过正向传播中的mask来实现激活函数层的反向传播（ReLU、sigmoid函数）

Tips.6 几何数学中的仿射变换对应的是神经网络中的Affine层  
矩阵乘法XW=Y对应的反向传播输出  
&emsp;1. 符号αL/αX=αL/αY*W^T  
&emsp;2. 符号αL/αW=X^T*αL/αY

Tips.7 如何用Python实现Affine层,如何根据正反向传播实现softmax函数的神经网络层softmax-with-loss层，神经网络的推理过程不需要softmax函数，而学习阶段则需要softmax函数