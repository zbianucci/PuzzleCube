hello='''
Hello! Welcome to Cube Solver by Zachary Bianucci
As of right now, there is no graphical interface,
so there are a few rules to prevent errors:
    
1. Please type in the Cube object as a list of
   lists that contains nine numbers ranging from
   0 to 5.
2. 6 represents an empty value
3. 0 to 5 correspond to the six different colors
   on a puzzle cube. 0 is white, 1 is orange, 2 is 
   green, 3 is red, 4 is blue, and 5 is yellow.
4. If you would
   like a default solved cube, please use Cube()
   without parameters. For a radomly scrambled cube,
   refer to the Scramble class and it will scramble
   one for you. Otherwise, for a specific scramble,
   please follow the strict guidelines stated above
   to prevent issues. I am working on creating a
   function that will check valid mixes.
'''
import random
import time
start_time=time.time()
print(hello)
class Cube:
    def __init__(self,cube_mix=[[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]):
        #checks to see that entered cube is valid
        self._valid_cube(cube_mix)
        self.cube_mix=cube_mix
    def _valid_cube(self,cube_mix):
        if type(cube_mix)!=list:
                raise TypeError("The object cube created is not a list.\nCube must be a list of lists with nine int within (numbers can range from 0 to 6)")
        for i in cube_mix:
            if type(i)!=list and len(i)!=6:
                raise TypeError("The object cube created is a list but does not have all lists for the interations.\nCube must be a list of lists with nine int within (numbers can range from 0 to 6)")
            for j in i:
                if type(j)!=int:
                    raise TypeError("The object cube is a list of lists but the elements are not of type int.\nCube must be a list of lists with nine int within (numbers can range from 0 to 6)")
                if j<0 or j>6:
                    raise TypeError("The object cube is a list of lists with type int, but all of those numbers do not range from 0 to 6.\nCube must be a list of lists with nine int within (numbers can range from 0 to 6)")
                    #cube must be a list of lists
        return True
    def set_cube(self,cube_mix=[[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]):
        self._valid_cube(cube_mix)         
        self.cube_mix=cube_mix
    def __str__(self):
        mix=""
        count1=0
        for i in range(len(self.cube_mix)):
            count1+=1
            count2=0
            for j in range(len(self.cube_mix[i])):
                count2+=1
                if (count1==1 or count1==6) and (count2==1 or count2==4 or count2==7):
                    mix+="       "
                if i==1 and j==0:
                    mix+=str(self.cube_mix[1][0])+" "+str(self.cube_mix[1][1])+" "+str(self.cube_mix[1][2])+"  "
                    mix+=str(self.cube_mix[2][0])+" "+str(self.cube_mix[2][1])+" "+str(self.cube_mix[2][2])+"  "
                    mix+=str(self.cube_mix[3][0])+" "+str(self.cube_mix[3][1])+" "+str(self.cube_mix[3][2])+"  "
                    mix+=str(self.cube_mix[4][0])+" "+str(self.cube_mix[4][1])+" "+str(self.cube_mix[4][2])+"\n"
                    
                    mix+=str(self.cube_mix[1][3])+" "+str(self.cube_mix[1][4])+" "+str(self.cube_mix[1][5])+"  "
                    mix+=str(self.cube_mix[2][3])+" "+str(self.cube_mix[2][4])+" "+str(self.cube_mix[2][5])+"  "
                    mix+=str(self.cube_mix[3][3])+" "+str(self.cube_mix[3][4])+" "+str(self.cube_mix[3][5])+"  "
                    mix+=str(self.cube_mix[4][3])+" "+str(self.cube_mix[4][4])+" "+str(self.cube_mix[4][5])+"\n"
                    
                    mix+=str(self.cube_mix[1][6])+" "+str(self.cube_mix[1][7])+" "+str(self.cube_mix[1][8])+"  "
                    mix+=str(self.cube_mix[2][6])+" "+str(self.cube_mix[2][7])+" "+str(self.cube_mix[2][8])+"  "
                    mix+=str(self.cube_mix[3][6])+" "+str(self.cube_mix[3][7])+" "+str(self.cube_mix[3][8])+"  "
                    mix+=str(self.cube_mix[4][6])+" "+str(self.cube_mix[4][7])+" "+str(self.cube_mix[4][8])+"\n"
                elif count1==1 or count1==6:
                    mix+=str(self.cube_mix[i][j])+" "
                if count2%3==0 and (count1==1 or count1==6):
                    mix+="\n"
            if count1==1 or count1==5:
                mix+="\n"
        return mix
    
class Move(Cube):
    def __init__(self, cube_mix=[[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]):
        Cube.__init__(self,cube_mix)
    def r(self,prime=False):
        #moves the right column stickers
        temp_column=[self.cube_mix[0][8],self.cube_mix[0][5],self.cube_mix[0][2]]
        for i in range(2,9,3):
            self.cube_mix[0][i]=self.cube_mix[2][i]
            self.cube_mix[2][i]=self.cube_mix[5][i]
        self.cube_mix[5][2]=self.cube_mix[4][6]
        self.cube_mix[5][5]=self.cube_mix[4][3]
        self.cube_mix[5][8]=self.cube_mix[4][0]
        for i in range(3):
            self.cube_mix[4][i*3]=temp_column[i]
        #rotates the right face stickers (corners)
        temp=self.cube_mix[3][0]
        self.cube_mix[3][0]=self.cube_mix[3][6]
        self.cube_mix[3][6]=self.cube_mix[3][8]
        self.cube_mix[3][8]=self.cube_mix[3][2]
        self.cube_mix[3][2]=temp
        #rotates the right face stickers (edges)
        temp=self.cube_mix[3][1]
        self.cube_mix[3][1]=self.cube_mix[3][3]
        self.cube_mix[3][3]=self.cube_mix[3][7]
        self.cube_mix[3][7]=self.cube_mix[3][5]
        self.cube_mix[3][5]=temp
        if prime:
            self.r(False)
            self.r(False)
    def r2(self):
        self.r()
        self.r()
    def l(self,prime=False):
        #moves the left column stickers
        temp_column=[self.cube_mix[0][0],self.cube_mix[0][3],self.cube_mix[0][6]]
        self.cube_mix[0][0]=self.cube_mix[4][8]
        self.cube_mix[0][3]=self.cube_mix[4][5]
        self.cube_mix[0][6]=self.cube_mix[4][2]
        
        self.cube_mix[4][2]=self.cube_mix[5][6]
        self.cube_mix[4][5]=self.cube_mix[5][3]
        self.cube_mix[4][8]=self.cube_mix[5][0]
        for i in range(0,9,3):
            self.cube_mix[5][i]=self.cube_mix[2][i]
        for i in range(3):
            self.cube_mix[2][i*3]=temp_column[i]
        #rotates the left face stickers (corners)
        temp=self.cube_mix[1][0]
        self.cube_mix[1][0]=self.cube_mix[1][6]
        self.cube_mix[1][6]=self.cube_mix[1][8]
        self.cube_mix[1][8]=self.cube_mix[1][2]
        self.cube_mix[1][2]=temp
        #rotates the left face stickers (edges)
        temp=self.cube_mix[1][1]
        self.cube_mix[1][1]=self.cube_mix[1][3]
        self.cube_mix[1][3]=self.cube_mix[1][7]
        self.cube_mix[1][7]=self.cube_mix[1][5]
        self.cube_mix[1][5]=temp
        if prime:
            self.l(False)
            self.l(False)
    def l2(self):
        self.l()
        self.l()
    def u(self,prime=False):
        #moves the top column stickers
        temp_column=[self.cube_mix[2][0],self.cube_mix[2][1],self.cube_mix[2][2]]
        for i in range(3):
            self.cube_mix[2][i]=self.cube_mix[3][i]
            self.cube_mix[3][i]=self.cube_mix[4][i]
            self.cube_mix[4][i]=self.cube_mix[1][i]
        for i in range(3):
            self.cube_mix[1][i]=temp_column[i]
        #rotates the top face stickers (corners)
        temp=self.cube_mix[0][0]
        self.cube_mix[0][0]=self.cube_mix[0][6]
        self.cube_mix[0][6]=self.cube_mix[0][8]
        self.cube_mix[0][8]=self.cube_mix[0][2]
        self.cube_mix[0][2]=temp
        #rotates the top face stickers (edges)
        temp=self.cube_mix[0][1]
        self.cube_mix[0][1]=self.cube_mix[0][3]
        self.cube_mix[0][3]=self.cube_mix[0][7]
        self.cube_mix[0][7]=self.cube_mix[0][5]
        self.cube_mix[0][5]=temp
        if prime:
            self.u(False)
            self.u(False)
    def u2(self):
        self.u()
        self.u()
    def d(self,prime=False):
        #moves the bottom column stickers
        temp_column=[self.cube_mix[3][6],self.cube_mix[3][7],self.cube_mix[3][8]]
        for i in range(6,9):
            self.cube_mix[3][i]=self.cube_mix[2][i]
            self.cube_mix[2][i]=self.cube_mix[1][i]
            self.cube_mix[1][i]=self.cube_mix[4][i]
        for i in range(3):
            self.cube_mix[4][i+6]=temp_column[i]
        #rotates the bottom face stickers (corners)
        temp=self.cube_mix[5][0]
        self.cube_mix[5][0]=self.cube_mix[5][6]
        self.cube_mix[5][6]=self.cube_mix[5][8]
        self.cube_mix[5][8]=self.cube_mix[5][2]
        self.cube_mix[5][2]=temp
        #rotates the bottom face stickers (edges)
        temp=self.cube_mix[5][1]
        self.cube_mix[5][1]=self.cube_mix[5][3]
        self.cube_mix[5][3]=self.cube_mix[5][7]
        self.cube_mix[5][7]=self.cube_mix[5][5]
        self.cube_mix[5][5]=temp
        if prime:
            self.d(False)
            self.d(False)
    def d2(self):
        self.d()
        self.d()
    def b(self,prime=False):
        #moves the back column stickers
        temp_column_0=[self.cube_mix[0][2],self.cube_mix[0][1],self.cube_mix[0][0]]
        temp_column_1=[self.cube_mix[1][0],self.cube_mix[1][3],self.cube_mix[1][6]]
        temp_column_5=[self.cube_mix[5][8],self.cube_mix[5][7],self.cube_mix[5][6]]
        temp_column_3=[self.cube_mix[3][2],self.cube_mix[3][5],self.cube_mix[3][8]]
        for i in range(3):
            self.cube_mix[1][i*3]=temp_column_0[i]
            self.cube_mix[5][i+6]=temp_column_1[i]
            self.cube_mix[3][i*3+2]=temp_column_5[i]
            self.cube_mix[0][i]=temp_column_3[i]
        #rotates the back face stickers (corners)
        temp=self.cube_mix[4][0]
        self.cube_mix[4][0]=self.cube_mix[4][6]
        self.cube_mix[4][6]=self.cube_mix[4][8]
        self.cube_mix[4][8]=self.cube_mix[4][2]
        self.cube_mix[4][2]=temp
        #rotates the back face stickers (edges)
        temp=self.cube_mix[4][1]
        self.cube_mix[4][1]=self.cube_mix[4][3]
        self.cube_mix[4][3]=self.cube_mix[4][7]
        self.cube_mix[4][7]=self.cube_mix[4][5]
        self.cube_mix[4][5]=temp
        if prime:
            self.b(False)
            self.b(False)
    def b2(self):
        self.b()
        self.b()
    def f(self,prime=False):
        #moves the front column stickers
        temp_column_0=[self.cube_mix[0][6],self.cube_mix[0][7],self.cube_mix[0][8]]
        temp_column_3=[self.cube_mix[3][6],self.cube_mix[3][3],self.cube_mix[3][0]]
        temp_column_5=[self.cube_mix[5][0],self.cube_mix[5][1],self.cube_mix[5][2]]
        temp_column_1=[self.cube_mix[1][8],self.cube_mix[1][5],self.cube_mix[1][2]]
        for i in range(3):
            self.cube_mix[3][i*3]=temp_column_0[i]
            self.cube_mix[5][i]=temp_column_3[i]
            self.cube_mix[1][i*3+2]=temp_column_5[i]
            self.cube_mix[0][i+6]=temp_column_1[i]
        #rotates the front face stickers (corners)
        temp=self.cube_mix[2][0]
        self.cube_mix[2][0]=self.cube_mix[2][6]
        self.cube_mix[2][6]=self.cube_mix[2][8]
        self.cube_mix[2][8]=self.cube_mix[2][2]
        self.cube_mix[2][2]=temp
        #rotates the front face stickers (edges)
        temp=self.cube_mix[2][1]
        self.cube_mix[2][1]=self.cube_mix[2][3]
        self.cube_mix[2][3]=self.cube_mix[2][7]
        self.cube_mix[2][7]=self.cube_mix[2][5]
        self.cube_mix[2][5]=temp
        if prime:
            self.f(False)
            self.f(False)
    def f2(self):
        self.f()
        self.f()
    def algorithmn(self, list_of_moves):
        prime = True
        for i in list_of_moves:
            prime = False
            if "\'" in i:
                prime = True
            if "R" in i:
                if "2" in i:
                    self.r2()
                else:
                    self.r(prime)
            elif "L" in i:
                if "2" in i:
                    self.l2()
                else:
                    self.l(prime)
            elif "U" in i:
                if "2" in i:
                    self.u2()
                else:
                    self.u(prime)
            elif "D" in i:
                if "2" in i:
                    self.d2()
                else:
                    self.d(prime)
            elif "F" in i:
                if "2" in i:
                     self.f2()
                else:
                     self.f(prime)
            elif "B" in i:
                if "2" in i:
                    self.b2()
                else:
                    self.b(prime)
    def __str__(self):
        return Cube.__str__(self)
class Scramble(Move):
    '''
    This class's sole purpose is to create a scrambled cube object that can be
    manipulated. The user should not have to call any of the methods in this
    class and only construct the object: a scrambled cube
    '''
    def __init__(self, num=20):
        self.num=num
        self.cube_mix=[[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5]]
        Move.__init__(self,self.cube_mix)
        self.list_of_moves=[]
        self.cube_mix=self.scramble_cube()
    def scramble_cube(self):
        for i in range(self.num):
            turn=random.randint(0,11)
            num2=random.randint(0,1)
            prime=False
            if num2==0:
                prime=True
            if turn==0:
                if not prime:
                    self.list_moves("R")
                else:
                    self.list_moves("R\'")
            elif turn==1:
                if not prime:
                    self.list_moves("L")
                else:
                    self.list_moves("L\'")
            elif turn==2:
                if not prime:
                    self.list_moves("U")
                else:
                    self.list_moves("U\'")
            elif turn==3:
                if not prime:
                    self.list_moves("D")
                else:
                    self.list_moves("D\'")
            elif turn==4:
                if not prime:
                    self.list_moves("F")
                else:
                    self.list_moves("F\'")
            elif turn==5:
                if not prime:
                    self.list_moves("B")
                else:
                    self.list_moves("B\'")
            elif turn==6:
                self.list_moves("R2")
            elif turn==7:
                self.list_moves("L2")
            elif turn==8:
                self.list_moves("U2")
            elif turn==9:
                self.list_moves("D2")
            elif turn==10:
                self.list_moves("F2")
            elif turn==11:
                self.list_moves("B2")
        Move.algorithmn(self,self.list_of_moves)
        return self.cube_mix
    def list_moves(self,rotation):
        self.list_of_moves.append(rotation)
    def __str__(self):
        return Move.__str__(self)
