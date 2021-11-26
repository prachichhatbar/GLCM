from django.shortcuts import render
import numpy as np
import requests

def output(request):
    return render(request, 'home.html')

def home(request):
    data=np.array(      [[0,1,2,3,0,1,2],
                    [1,2,3,0,1,2,3],
                    [2,3,0,1,2,3,0],
                    [3,0,1,2,3,0,1],
                    [0,1,2,3,0,1,2],
                    [1,2,3,0,1,2,3],
                    [2,3,0,1,2,3,0]     ])

    def search_max(m):
        a=[]
        for i in range(len(m)):
            a.append(max(m[i]))
        MAX=max(a)
        return MAX
    def GLCM(m,l,A,scale): 
        glcm=np.zeros((scale, scale))
        d=len (m)
        for i in range (scale):
            for j in range (scale):
                for x in range(d):
                    for y in range (d):
                        if A==0:
                            if y+1<d:
                                if m[x][y]==i and m[x][y+1]==j:#
                                    glcm[i][j]+=1
                        elif A==45:
                            if 0<=(x-1) and y+l<d:#EHAT
                                if m[x][y]==i and m[x-1][y+1]==j:
                                    glcm[i][j]+=1
                        elif A==90:
                            if x+l<d:
                                if m[x][y]==i and m[x+l][y]==j:
                                    glcm[i][j]+=1
                        elif A==135:
                            if 0<=(x-1) and 0<y-l<d:#E4D
                                if m[x][y]==i and m[x-l][y-l]==j:
                                    glcm[i][j]+=1
        return glcm
    scale=search_max(data) +1
    a=GLCM (data,2,0, scale)
    b=GLCM (data, 2,45, scale)
    c=GLCM(data, 2,90, scale)
    d=GLCM(data, 2, 135, scale)
    print('0°: \n',a)
    print('45°: \n',b)
    print('90°: \n',c)
    print('135°: \n',d)  
    return render(request, 'home.html',{"0\n":a,"45\n":b,"90\n":c,"135\n":d})