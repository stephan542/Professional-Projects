package Pacman;

import java.awt.Color;
import java.awt.Graphics;
import java.util.HashMap;

import nn.NeuralNetwork;


public class Player implements Comparable<Player> {

    public int  HEIGHT = 623;
    public int  WIDTH = 690;

    public int x, y, w, xv, yv, speed,gy,gx;
    public NeuralNetwork brain;
    public double fitness,score,distancetoG;
    public HashMap<String,Wall> walls;
    public Color color;

    public Player(int x, int y,int gx,int gy,Player player) {
        this.x = x;
        this.y = y;
        this.w = 31;
        this.xv = 0;
        this.yv = 0;
        this.color = player.color;
        this.speed = 2;
        this.walls = player.walls;
        this.gx = gx;
        this.gy = gy;
        this.distancetoG = distance(gx, gy);
        this.brain = player.brain.copy();
    }

    public Player(Player player,int sx,int sy,int gx,int gy) {
        this.x = sx;
        this.y = sy;
        this.w = 31;
        this.xv = 0;
        this.yv = 0;
        this.speed = 2;
        this.walls = player.walls;
        this.gx = gx;
        this.gy = gy;
        this.color = player.color;
        this.distancetoG = distance(gx, gy);
        this.brain = player.brain.copy();
    }
    public Player(int x, int y,HashMap<String,Wall> walls,int gx,int gy) {
        this.x = x;
        this.gx = gx;
        this.gy= gy;
        this.y = y;
        this.w = 31;
        this.xv = 0;
        this.yv = 0;
        this.speed = 2;
        this.walls = walls;
        this.brain = new NeuralNetwork(10,16,4);
        this.color = Color.RED;
        this.distancetoG = distance(gx, gy);
    }

    public void up() {
        this.yv = -this.speed;
    }

    public void down() {
        this.yv = this.speed;
    }

    public void left() {
        this.xv = -this.speed;
    }

    public void right() {
        this.xv = this.speed;
    }

    public void draw(Graphics g) {
        // System.out.println(this.x+"x"+this.y)
        g.setColor(this.color);
        g.drawRect(this.x, this.y, this.w, this.w);
        g.fillOval(this.x, this.y, this.w, this.w);
        //g.setColor(Color.GREEN);
        //g.drawLine(this.x+this.w/2, this.y+this.w/2, gx, gy);
    }

    public void mutate() {
        this.brain.mutate(0.2);
    }
    public void mutate(double u) {
        this.brain.mutate(u);
    }

    public void update() {
        int xposition, yposition, xposition2, yposition2;
        double s = 0;
        s = this.distancetoG - this.distance(this.gx,this.gy);
        this.score = s<0?0:s;

        for (int i = this.x; i < this.x +this.w; i++) {
            yposition = this.y + this.yv;
            yposition2 = yposition + this.w;
            if (this.walls.get(i + "x" + yposition) != null || this.walls.get(i + "x" + yposition2) != null) {
                this.yv = 0;
            }
        }

        for (int j = this.y; j < this.y+ this.w; j++) {
            xposition = this.x + this.xv;
            xposition2 = xposition + this.w;
            if (this.walls.get(xposition + "x" + j) != null || this.walls.get(xposition2 + "x" + j) != null) {
                this.xv = 0;
            }
        }

        this.x += this.xv;
        this.y += this.yv;

        if(this.x < 0){
            this.x = 600;
        }
        if(this.x > 600){
            this.x = 0;
        }
    }

    public void think(Graphics g){
        double[] inputs = new double[10];
    
        double maxout = 0;
        int maxindex =0;

        // inputs[0] = this.see(-1, -1, 0, 0,g) / HEIGHT;
        // inputs[1] = this.see(0, -1, this.w / 2, 0,g) / HEIGHT;
        // inputs[2] = this.see(1, -1, this.w, 0,g) / HEIGHT;
        // inputs[3] = this.see(-1, 0, 0, this.w / 2,g) / WIDTH;
        // inputs[4] = this.see(-1, 1, 0, this.w,g) / HEIGHT;
        // inputs[5] = this.see(0, 1, this.w / 2, this.w,g)  / HEIGHT;
        // inputs[6] = this.see(1, 1, this.w, this.w,g) / HEIGHT;
        // inputs[7] = this.see(1, 0, this.w, this.w / 2,g)  / WIDTH;

        inputs[0] = this.see(0, -1, 0, 0,g) / HEIGHT;
        inputs[1] = this.see(0, -1, this.w, 0,g) / HEIGHT;
        inputs[2] = this.see(1, 0, this.w, 0,g) / WIDTH;
        inputs[3] = this.see(-1, 0, 0, 0,g) / WIDTH;
        inputs[4] = this.see(-1, 0, 0, this.w,g) / WIDTH;
        inputs[5] = this.see(0, 1, 0, this.w,g)  / HEIGHT;
        inputs[6] = this.see(0, 1, this.w, this.w,g) / HEIGHT;
        inputs[7] = this.see(1, 0, this.w, this.w,g)  / WIDTH;

        inputs[8] = Math.abs(this.gx - this.x)/WIDTH;
        inputs[9] = Math.abs(this.gy - this.y)/HEIGHT;

        double [] output = brain.predict(inputs);

        for(int i=0;i<output.length;i++){
            if(output[i]>maxout){
                maxindex = i;
                maxout = output[i];
            }
        }

        if(maxindex == 1){
            this.up();
        }else if(maxindex == 2){
            this.down();
        }else if(maxindex == 3){
            this.left();
        }else{
            this.right();
        }
    }

    public double see(int s, int s2, int c1, int c2,Graphics g) {
        int newx, newy;
        //int oldx,oldy;
        int t = 0;
        newx = this.x + (t * s) + c1;
        newy = this.y + (t * s2) + c2;
        // oldx = this.x + (0 * s) + c1;
        // oldy = this.y + (0 * s2) + c2;

        for (t = 0;t<200; t++) {
            newx = this.x + (t * s) + c1;
            newy = this.y + (t * s2) + c2;
            //g.drawLine(oldx, oldy, newx, newy);
            if(this.walls.get(newx + "x" + newy) != null){
                return t;
            }
        }
        return 0;
    }

    public double distance(int x2, int y2) {
        int rise = Math.abs((y2 - this.y));
        int run = Math.abs((x2 - this.x));
        return Math.sqrt(Math.pow(rise, 2) + Math.pow(run, 2));
    }

    public int compareTo(Player p) {
        if(p.fitness > this.fitness){
            return 1;
        }else if(p.fitness<this.fitness){
            return -1;
        }else{
            if(p.score<this.fitness){
                return 1;
            }else if(p.score<this.fitness){
                return -1;
            }
        }
        return 0;
    }

}