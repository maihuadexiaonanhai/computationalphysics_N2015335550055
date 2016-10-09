# **第四次作业**
## *问题*
 - Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are  
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}=\frac{N_B}{\tau_B}-\frac{N_A}{\tau_A}" alt="" title="" />  
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}=\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B}" alt="" title="" />  
where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.  

## *摘要*
因为有两个常微分方程，所以我们可以用欧拉方法来解决这个问题。首先我们要解决的第一个方程中的二次及高次方程的泰勒展开，这意味着我们只需要它的线性项。这可以很好的近似两个方程。为了实现它，我们必须完成4个步骤：             
 - 确定必要的变量            
 - 初始化所有的变量和参数            
 - 做计算
 - 存储结果
 
此外，我们可以使用不同的初始条件，以确保我们编程的可靠性。

## *介绍*
### 分析
 - 求解两个方程，首先我们用泰勒展开 <img src="http://latex.codecogs.com/gif.latex?U_A" alt="" title="" /> 和 <img src="http://latex.codecogs.com/gif.latex?U_B" alt="" title="" /> 如下： 
![](http://latex.codecogs.com/gif.latex?N_U%28t&plus;%5CDelta%20t%29%3DN_U%28t%29&plus;%5Cfrac%7BdN_U%7D%7Bdt%7D%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7Bd%5E2%20N_U%7D%7Bdt%5E2%7D%28%5CDelta%20t%29%5E2&plus;...)  
 - 使用近似 
![](http://latex.codecogs.com/gif.latex?N_U%28t&plus;%5CDelta%20t%29%5Capprox%20N_U%28t%29&plus;%5Cfrac%7BdN_U%7D%7Bdt%7D%5CDelta%20t)
 - 在问题中使用方程来代替<img src="http://latex.codecogs.com/gif.latex?\frac{dN_U}{dt}" alt="" title="" /> ，并使用各种初始条件得到曲线
 - 然后我们用代码来实现它

## *程序*
#### 核a与核b的衰变
 - 创建一个类（[Ex_3-1.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-1.py)）
 - 初始化类，并设置它的初始参数和属性（[Ex_3-2.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-2.py)）。
 初始条件如下:
 核a初始数->100
 核b初始数->0
 时间常数->1
 时间步长->0.05
 总时间->5
 - 定义函数来计算（设计循环附加我们下面做的列表计算）（[Ex_3-3.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-3.py)）：
 - 定义函数显示PyLab结果（[Ex_3-4.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-4.py)）： 
 - 定义存储结果的函数（[Ex_3-5.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-5.py)）： 
 - 在类中创建对象并实现我们之前定义的函数（[Ex_3-6.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-6.py)）：

#### 不同初始条件下三组原子核的衰变
 - 使用不同的初始条件再进行计算，连同我们以前使用的初始条件绘制（[Ex_3-7.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-7.py)）：
核a初始数 -> 100   
核b初始数 -> 0
核c初始数 -> 100   
核d初始数 -> 50 
核e初始数 -> 100
核f初始数 -> 30
时间常数 -> 1
时间步长 -> 0.05
总时间 -> 5 
#### 对核a和核b衰变在同一组使用不同的步数 
 - 使用不同数量的步骤来计算和检查结果初始条件为（[Ex_3-8.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-8.py)）：
核a初始数 -> 100 
核b初始数 -> 0
时间常数 -> 1
时间step1 -> 0.1
时间step2 -> 0.001
总时间 -> 5

#### 对问题进行测试
初始条件（[Ex_3-9.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-9.py)）： 
核a初始数->100        
核b初始数->0         
时间常数->1          
时间步长->0.1     
总时间->5 
我们用分析的解决方案来为程序做测试。 
![Ex_P1.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P1.png)
## *绘图*
 - 衰变的核a和核在一组的问题（[Ex_3-10.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-10.py)）          
初始条件：             
核a初始数 -> 100初始数             
核b初始数 -> 0初始数             
时间常数 -> 1             
时间步长 -> 0.05             
总时间 -> 5 
![Ex_P2.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P2.png)
 - 不同初始条件下三组原子核的衰变（[Ex_3-11.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-11.py)）             
注意，核a和核b是一组，核c和核d在第二组，核e和核f都在第三组，初始条件：             
核a初始数 -> 100   
核b初始数 -> 0
核c初始数 -> 100   
核d初始数 -> 50 
核e初始数 -> 100
核f初始数 -> 30
时间常数 -> 1
时间步长 -> 0.05
总时间 -> 5 
![Ex_P3.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P3.png)
 - 使用不同步骤的同一组中两个核衰变的计算（[Ex_3-12.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-12.py)）
初始条件：             
核a初始数 -> 100 
核b初始数 -> 0
时间常数 -> 1
时间step1 -> 0.1
时间step2 -> 0.001
总时间 -> 5
![Ex_P4.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P4.png)

## *结果*
 - 无论核a和核b的初始值为多少，核a的数量趋于减少，核b数量有增加的趋势，很长一段时间后他们都将达到平衡点。             
 - 我们做的步骤越多，结果越精确。

## *致谢*
 - 感谢弘毅班大神的无私奉献！
