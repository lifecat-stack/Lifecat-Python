package com.testone;

import javax.swing.*;
import java.awt.*;

/**
 * 程序入口
 */
public class MainTest {
    private static int vertex_size;
    private static int connection_radiu;
    private static VertexMatrix table;
    private static VertexFactory factory;
    private static Vertex[] vset;

    public static void main(String[] args) throws InterruptedException {
        init();

        for (int i = 0; i < 2; i++) {
            Runnable r=new Runnable() {
                @Override
                public void run() {
                    createMatrix();
                    createVertexs();

                    calculateMatrix();

                    createVertexFrame();

                    createDataFrame();

                    table.show();
                }
            };

            Thread t=new Thread(r);
            t.start();

            t.sleep(1000);

            vertex_size=vertex_size+50;
            connection_radiu=connection_radiu+50;
        }
    }


    //1、初始化节点个数和通信半径
    private static void init() {
        vertex_size = 50;
        connection_radiu = 100;
    }

    //2、创建并初始化一阶邻接矩阵
    private static void createMatrix() {
        table = new VertexMatrix(vertex_size);
    }

    //3、创建顶点的集合
    private static void createVertexs() {
        factory = new VertexFactory(vertex_size);
        vset = factory.createVertexSet();

    }

    //4、计算邻接矩阵
    private static void calculateMatrix() {
        for (int i = 0; i < vertex_size; i++) {
            for (int j = i; j < vertex_size; j++) {
                if (vset[i].isConnection(vset[j], connection_radiu)) {
                    table.makeValue(i, j);
                }
            }
        }
    }

    //5、生成网络节点图
    private static void createVertexFrame() {
        //WSN网络图
        EventQueue.invokeLater(() -> {
            NetworkFrame network = new NetworkFrame();
            network.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            network.setVisible(true);
        });
    }

    //6、生成结果数据图
    private static void createDataFrame() {
        EventQueue.invokeLater(() -> {
            DataFrame network = new DataFrame();
            network.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            network.setVisible(true);
        });
    }

}

