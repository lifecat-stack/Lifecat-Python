package com.testone;

/**
 * 创建无向图的邻接矩阵
 */
public class VertexMatrix {
    private static int [][] P_table;

    //创建并初始化一阶邻接矩阵
    public VertexMatrix(int size){
        this.P_table=new int[size][size];
        for (int i = 0; i < P_table.length; i++) {
            for (int j = 0; j < P_table.length; j++) {
                P_table[i][j]=0;
            }
        }
    }

    //将连通的边置为1
    public void makeValue(int i,int j){
        P_table[i][j]=1;
    }

    //打印邻接矩阵
    public void show() {
        for (int i = 0; i < P_table.length; i++) {
            for (int j = 0; j < P_table.length; j++) {
                System.out.print(P_table[i][j]+" ");
            }
            System.out.println();
        }
    }

    public static int[][] getP_table() {
        return P_table;
    }
}
