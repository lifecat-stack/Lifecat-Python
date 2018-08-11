package com.testone;

import javax.swing.*;

public class DataFrame extends JFrame {
    private DataCanves canves;

    private static final int NET_WIDTH=700;
    private static final int NET_HEIGHT=700;

    public DataFrame(){
        canves=new DataCanves();
        this.setLocation(1000,100);
        this.setSize(NET_WIDTH,NET_HEIGHT);
        this.add(canves);
    }
}
