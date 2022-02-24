import re
class Map:
    def __init__(self,width,height,chess=[]):
        self.width=width
        self.height=height
        self.chess=chess
    def genMap(self):#马晨源 1/9
        for i in range(self.height):
            for j in range(self.width):
                pos=j+self.width*i
                if i==0 and j==0:
                    if j==0:
                        if s[i][j]=='0':pass
                        elif s[i][j]=='1':self.chess[pos].setTop()
                        elif s[i][j]=='2':self.chess[pos].setLeft()
                        elif s[i][j]=='3':self.chess[pos].setTop();self.chess[pos].setLeft()
                else:
                    if i==0:
                        if s[i][j]=='0':pass
                        elif s[i][j]=='1':
                            self.chess[pos].setTop()
                            self.chess[pos-1].setRight()#左边元素的右边是True
                        elif s[i][j]=='2':self.chess[pos].setLeft()
                        elif s[i][j]=='3':
                            self.chess[pos].setTop()
                            self.chess[pos].setLeft()
                            self.chess[pos-1].setRight()#左边元素的右边是True
                    elif j==0:
                        if s[i][j]=='0':pass
                        elif s[i][j]=='1':
                            self.chess[pos].setTop()
                            self.chess[pos-self.width].setBottom()#上面元素的底部是True
                        elif s[i][j]=='2':self.chess[pos].setLeft()
                        elif s[i][j]=='3':
                            self.chess[pos].setTop()
                            self.chess[pos].setLeft()
                            self.chess[pos-width].setBottom()#上面元素的底部是True

                    else:
                        if s[i][j]=='0':pass
                        elif s[i][j]=='1':
                            self.chess[pos].setLeft()
                            self.chess[pos-self.width].setBottom()#上面元素的底部是True
                            #pos=y+width*x
                        elif s[i][j]=='2':
                            self.chess[pos].setLeft()
                            self.chess[pos-1].setRight()#左边元素的右边是True
                        elif s[i][j]=='3':
                            self.chess[pos].setTop()
                            self.chess[pos].setLeft()
                            self.chess[pos-1].setRight()#左边元素的右边是True
                            self.chess[pos-self.width].setBottom()#上面元素的底部是True
        return self.chess
    def preBox(self):
        for i in self.chess:
            if i.x==self.width-1 or i.y==self.height-1:
                self.chess[i.y+width*i.x]
        return self.chess
    def isdoor(self):#马晨源 1/9
        for i in self.chess:
            if i.x!=height-1 and i.y!=width-1:
                if i.x==0 and (not i.top):
                    i.door=True
                if i.x==self.height-2 and (not i.top):
                    i.door=True
                if i.y==0 and (not i.left):
                    i.door=True
                if i.y==self.width-2 and (not i.right):
                    i.door=True
    def isForkWindowsNumber(self):#辨别岔路口，找出‘窗’的个数
        for i in self.chess:
            count = 0
            if i.x==0:
                if i.y==0:
                    if i.right:count+=1
                    if i.bottom:count+=1
                    i.windows=count
                    if count>2:
                        i.setFork()
                else:
                    if i.bottom:count+=1
                    if i.left:count+=1
                    if i.right:count+=1
                    i.windows=count
                    if count>2:
                        i.setFork()
            elif i.y==0:
                if i.top:count+=1
                if i.bottom:count+=1
                if i.right:count+=1
                i.windows=count
                if count>2:
                    i.setFork()
            else:
                if i.top:count+=1
                if i.bottom:count+=1
                if i.left:count+=1
                if i.right:count+=1
                i.windows=count
                if count>2:
                    i.setFork()
    def optDoor(self):
        doors=[]
        print('门的位置是：', end='')
        for i in self.chess:
            if i.door:
                doors.append(i)
                print('(%s,%s)'%(i.x,i.y),end='')
        print('\n')
        return doors
    # def optPath(self):#马晨源1/11     找路径
    #     doors = self.optDoor()
    #     for door in doors:
    #         print(type(door))
    #         print('目前的门是：%s，%s'%(door.x,door.y))
    #         path=self.move(door, doors, [], [], [door])
            
    #         print(path)
    #         if len(path)==1:
    #             # print("门(%s,%s)有唯一路径:%s"%s(door.x,door.y),end='')
    #             print(path)
    # def nextStep(self,step,history):#马晨源1/11
    
    #     print(step.x,step.y)
    #     y = step.y;x = step.x;pos = y + self.width * x
    #     if step.x==0:#如果当前步在第一行，则不用判断上边界
    #         if step.x==0 and step.y==0:#如果当前步在0,0，则不用判断上边界和左边界
    #             if step.right == False:
    #                 nextStep = self.chess[pos + 1]
    #                 if nextStep not in history:
    #                     return nextStep
    #             if step.bottom == False:
    #                 nextStep = self.chess[pos + self.width]
    #                 if nextStep not in history:
    #                     return nextStep
    #         else:
    #             if step.left == False:
    #                 nextStep = self.chess[pos - 1]
    #                 if nextStep not in history:
    #                     print(nextStep.x,nextStep.y)
    #                     return nextStep
    #             if step.right == False:
    #                 nextStep = self.chess[pos + 1]
    #                 if nextStep not in history:
    #                     return nextStep
    #             if step.bottom == False:
    #                 nextStep = self.chess[pos + self.width]
    #                 if nextStep not in history:
    #                     return nextStep
    #     elif step.y==0:#如果当前步在第一列，则不用判断左边界
    #         if step.left == False:
    #             nextStep = self.chess[pos - 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.right == False:
    #             nextStep = self.chess[pos + 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.bottom == False:
    #             nextStep = self.chess[pos + self.width]
    #             if nextStep not in history:
    #                 return nextStep
    #     elif step.x==self.height-2:
    #         if step.left == False:
    #             nextStep = self.chess[pos - 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.right == False:
    #             nextStep = self.chess[pos + 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.top == False:
    #             nextStep = self.chess[pos - self.width]
    #             if nextStep not in history:
    #                 return nextStep
    #     elif step.y==self.width-2:
    #         if step.left == False:
    #             nextStep = self.chess[pos - 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.top == False:
    #             nextStep = self.chess[pos - self.width]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.bottom == False:
    #             nextStep = self.chess[pos + self.width]
    #             if nextStep not in history:
    #                 return nextStep
    #     else:
    #         if step.left == False:
    #             nextStep = self.chess[pos - 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.right == False:
    #             nextStep = self.chess[pos + 1]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.top == False:
    #             nextStep = self.chess[pos - self.width]
    #             if nextStep not in history:
    #                 return nextStep
    #         if step.bottom == False:
    #             nextStep = self.chess[pos + self.width]
    #             if nextStep not in history:
    #                 return nextStep
    # def move(self,step,doors,history,path,steps):#马晨源1/11
    #     print(type(step))
    #     print(step.x,step.y)
    #     print(step.windows)
    #     if step.windows>=2:#有路可走
    #         nextStep=self.nextStep(step,history)#生成没走过的下一步
    #         if nextStep in doors:
    #             #如果下一步是“门”，则先把这个门加入路径，再将路径输出到列表里，将路径逐个出栈，直到原来的交叉点
    #             steps.append(nextStep)
    #             history.append(nextStep)
    #             path.append(steps)
    #             print(steps)
    #             while len(steps)!=0:
    #                 print(len(steps))
    #                 if steps[len(steps) - 1].fork != True:
    #                     steps.pop()
    #                 if len(steps)!=0:
    #                     return self.move(steps[len(steps)-1],doors,history,path,steps)#到了交叉点，用交叉点的坐标进行移动
    #             return path
    #         else:#不是门呢？
    #             steps.append(nextStep)
    #             history.append(nextStep)
    #             return self.move(nextStep, doors, history, path, steps)
                
                
    #     else:#无路可走，死胡同，逐个出栈，直到原来的交叉点
    #         while len(steps)!=0:
    #             if steps[len(steps) - 1].fork != True:
    #                 steps.pop()
    #             if len(steps) != 0:
    #                 print(steps)
    #                 print(steps[len(steps)-1])
    #                 return self.move(steps[len(steps)-1], doors, history, path, steps)  # 到了交叉点，用交叉点的坐标进行移动
    #         return path
class Box:#马晨源 1/9
    def __init__(self,x,y,left=False,top=False,right=False,bottom=False,door=False,fork=False,windows=0):
        self.x=x;self.y=y;self.left=left;self.right=right;self.top=top;self.bottom=bottom;self.door=door
        self.fork=fork;self.windows=windows
    def setLeft(self):self.left=True
    def setRight(self):self.right = True
    def setTop(self):self.top = True
    def setBottom(self):self.bottom = True
    def setDoor(self):self.door=True
    def setFork(self):self.fork=True

def iptBlock(width,height):#马晨源1/9
    chess=[]
    for i in range(height):
        for j in range(width):
            chess.append(Box(i,j))
    return chess
def file(f):#李欢
    fp = open(f)#读取文件并去除空格和多余的换行
    content = fp.read()
    content = content.replace(' ', '')
    s = re.split('\n', content)
    while '' in s:
        s.remove('')
    return s








if __name__ == '__main__':
    # choice=input('你想看第几个文件？')
    choice=1
    f=r'maze_'+str(choice)+'.txt'
    s=file(f)#预处理
    width=len(s[0]);height=len(s)
    m=iptBlock(width,height)
    mp=Map(width,height,m)
    mp.genMap()
    mp.preBox()
    mp.isdoor()
    mp.isForkWindowsNumber()
    mp.optDoor()
    # mp.optPath()