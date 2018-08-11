package com.testone;

import javax.swing.*;
import java.awt.*;
/**
 * 绘制网络节点图
 */
public class NetCanves extends Canvas{
    // 画布原点坐标
    protected static final int Origin_X = 100;
    protected static final int Origin_Y = 100;

    // 画布终点坐标
    private static final int XAxis_X = 600;
    private static final int XAxis_Y = Origin_Y;
    private static final int YAxis_X = Origin_X;
    private static final int YAxis_Y = 600;

    private Vertex[] vset;
    private int[][] p_matrix;

    public NetCanves() {
        super();
        vset=VertexFactory.getV_set();
        p_matrix=VertexMatrix.getP_table();
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        Graphics2D g2D = (Graphics2D) g;
        Color c = new Color(200, 70, 0);
        g.setColor(c);
        //绘图提示-消除锯齿
        g2D.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        // 画坐标轴
        g2D.setStroke(new BasicStroke(Float.parseFloat("2.0F")));// 轴线粗度

        // 上边
        g.drawLine(Origin_X, Origin_Y, XAxis_X, XAxis_Y);
        // 下边
        g.drawLine(YAxis_X, YAxis_Y, XAxis_X, YAxis_Y);
        // 左边
        g.drawLine(Origin_X, Origin_Y, YAxis_X, YAxis_Y);
        // 右边
        g.drawLine(XAxis_X, XAxis_Y, XAxis_X, YAxis_Y);

        //绘制随机的节点图
        for (int i = 0; i < vset.length; i++) {
            g.fillRect(vset[i].getX(),vset[i].getY(),5,5);
        }

        //连线
        Color edge = new Color(20, 200, 60);
        g.setColor(c);
        g2D.setStroke(new BasicStroke(Float.parseFloat("1.0F")));

        for (int i = 0; i < p_matrix.length; i++) {
            for (int j = i+1; j < p_matrix.length; j++) {
                if (p_matrix[i][j]!=0){
                    g.drawLine(vset[i].getX(),vset[i].getY(),vset[j].getX(),vset[j].getY());
                }
            }
        }
    }
}
