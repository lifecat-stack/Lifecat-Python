package com.testone;

import javax.swing.*;

/**
 * 创建V的网络图
 */
public class NetworkFrame extends JFrame{
    private NetCanves canves;

    private static final int NET_WIDTH=700;
    private static final int NET_HEIGHT=700;


    public NetworkFrame(){
        canves=new NetCanves();
        this.setLocation(100,100);
        this.setSize(NET_WIDTH,NET_HEIGHT);
        this.add(canves);
    }
}
