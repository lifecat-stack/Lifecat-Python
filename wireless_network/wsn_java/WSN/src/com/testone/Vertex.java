package com.testone;

/**
 * V对象
 */
public class Vertex {
    private int x,y;
    private int id;

    //随机生成位置
    public Vertex(int id){
        this.id=id;
        this.x= (int) (Math.random()*500)+100;
        this.y= (int) (Math.random()*500)+100;
    }

    //判断通信距离为R时，两点间是否连通
    public boolean isConnection(Vertex v2,int R){
        if (((this.x-v2.x)*(this.x-v2.x)+(this.y-v2.y)*(this.y-v2.y))<=R*R){
            return true;
        }
        return false;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
