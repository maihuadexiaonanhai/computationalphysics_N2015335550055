# **���Ĵ���ҵ**
## *����*
 - Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are  
			<img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}=\frac{N_B}{\tau_B}-\frac{N_A}{\tau_A}" alt="" title="" />  
			<img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}=\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B}" alt="" title="" />  
where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.  

## *ժҪ*
��Ϊ��������΢�ַ��̣��������ǿ�����ŷ�����������������⡣��������Ҫ����ĵ�һ�������еĶ��μ��ߴη��̵�̩��չ��������ζ������ֻ��Ҫ�������������ԺܺõĽ����������̡�Ϊ��ʵ���������Ǳ������4�����裺             
 - ȷ����Ҫ�ı���            
 - ��ʼ�����еı����Ͳ���            
 - ������
 - �洢���
���⣬���ǿ���ʹ�ò�ͬ�ĳ�ʼ��������ȷ�����Ǳ�̵Ŀɿ��ԡ�

## *����*
### ����
 - ����������̣�����������̩��չ�� <img src="http://latex.codecogs.com/gif.latex?U_A" alt="" title="" /> �� <img src="http://latex.codecogs.com/gif.latex?U_B" alt="" title="" /> ���£� 
![](http://latex.codecogs.com/gif.latex?N_U%28t&plus;%5CDelta%20t%29%3DN_U%28t%29&plus;%5Cfrac%7BdN_U%7D%7Bdt%7D%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7Bd%5E2%20N_U%7D%7Bdt%5E2%7D%28%5CDelta%20t%29%5E2&plus;...)  
 - ʹ�ý��� 
![](http://latex.codecogs.com/gif.latex?N_U%28t&plus;%5CDelta%20t%29%5Capprox%20N_U%28t%29&plus;%5Cfrac%7BdN_U%7D%7Bdt%7D%5CDelta%20t)
 - ��������ʹ�÷���������<img src="http://latex.codecogs.com/gif.latex?\frac{dN_U}{dt}" alt="" title="" /> ����ʹ�ø��ֳ�ʼ�����õ�����
 - Ȼ�������ô�����ʵ����

## *����*
#### ��a���b��˥��
 - ����һ���ࣨ[Ex_3-1.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-1.py)��
 - ��ʼ���࣬���������ĳ�ʼ���������ԣ�[Ex_3-2.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-2.py)����
��ʼ�������£�
��a��ʼ��->100        
��b��ʼ��->0         
ʱ�䳣��->1          
ʱ�䲽��->0.05      
��ʱ��->5 
 - ���庯�������㣨���ѭ�������������������б���㣩��[Ex_3-3.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-3.py)����
 - ���庯����ʾPyLab�����[Ex_3-4.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-4.py)���� 
 - ����洢����ĺ�����[Ex_3-5.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-5.py)���� 
 - �����д�������ʵ������֮ǰ����ĺ�����[Ex_3-6.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-6.py)����

#### ��ͬ��ʼ����������ԭ�Ӻ˵�˥��
 - ʹ�ò�ͬ�ĳ�ʼ�����ٽ��м��㣬��ͬ������ǰʹ�õĳ�ʼ�������ƣ�[Ex_3-7.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-7.py)����
��a��ʼ�� -> 100   
��b��ʼ�� -> 0
��c��ʼ�� -> 100   
��d��ʼ�� -> 50 
��e��ʼ�� -> 100
��f��ʼ�� -> 30
ʱ�䳣�� -> 1
ʱ�䲽�� -> 0.05
��ʱ�� -> 5 
#### �Ժ�a�ͺ�b˥����ͬһ��ʹ�ò�ͬ�Ĳ��� 
 - ʹ�ò�ͬ�����Ĳ���������ͼ������ʼ����Ϊ��[Ex_3-8.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-8.py)����
��a��ʼ�� -> 100 
��b��ʼ�� -> 0
ʱ�䳣�� -> 1
ʱ��step1 -> 0.1
ʱ��step2 -> 0.001
��ʱ�� -> 5

#### ��������в���
��ʼ������[Ex_3-9.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-9.py)���� 
��a��ʼ��->100        
��b��ʼ��->0         
ʱ�䳣��->1          
ʱ�䲽��->0.1     
��ʱ��->5 
�����÷����Ľ��������Ϊ���������ԡ� 
![Ex_P1.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P1.png)
## *��ͼ*
 - ˥��ĺ�a�ͺ���һ������⣨[Ex_3-10.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-10.py)��          
��ʼ������             
��a��ʼ�� -> 100��ʼ��             
��b��ʼ�� -> 0��ʼ��             
ʱ�䳣�� -> 1             
ʱ�䲽�� -> 0.05             
��ʱ�� -> 5 
![Ex_P2.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P2.png)
 - ��ͬ��ʼ����������ԭ�Ӻ˵�˥�䣨[Ex_3-11.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-11.py)��             
ע�⣬��a�ͺ�b��һ�飬��c�ͺ�d�ڵڶ��飬��e�ͺ�f���ڵ����飬��ʼ������             
��a��ʼ�� -> 100   
��b��ʼ�� -> 0
��c��ʼ�� -> 100   
��d��ʼ�� -> 50 
��e��ʼ�� -> 100
��f��ʼ�� -> 30
ʱ�䳣�� -> 1
ʱ�䲽�� -> 0.05
��ʱ�� -> 5 
![Ex_P3.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P3.png)
 - ʹ�ò�ͬ�����ͬһ����������˥��ļ��㣨[Ex_3-12.py](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_3-12.py)��
��ʼ������             
��a��ʼ�� -> 100 
��b��ʼ�� -> 0
ʱ�䳣�� -> 1
ʱ��step1 -> 0.1
ʱ��step2 -> 0.001
��ʱ�� -> 5
![Ex_P4.png](https://github.com/maihuadexiaonanhai/computationalphysics_N2015335550055/blob/master/Exercise_03/Ex_P4.png)

## *���*
 - ���ۺ�a�ͺ�b�ĳ�ʼֵΪ���٣���a���������ڼ��٣���b���������ӵ����ƣ��ܳ�һ��ʱ������Ƕ����ﵽƽ��㡣             
 - �������Ĳ���Խ�࣬���Խ��ȷ��

## *��л*
 - ��л�����������˽���ף�