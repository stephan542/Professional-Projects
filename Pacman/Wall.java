package Pacman;

import java.awt.Color;
import java.awt.Graphics;

public class Wall {
    public int x,y;

    public Wall(int x,int y){
        this.x = x;
        this.y = y;
    }

    public void draw(Graphics g){
        g.setColor(Color.WHITE);
        g.drawLine(this.x, this.y, this.x,this.y);
    }

    public void hits(int mx,int my){
        if(mx==this.x && my==this.y){
            System.out.println("Hit");
        }
    }

    public String toString(){
        return "1";
    }
}