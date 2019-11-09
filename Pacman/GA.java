package Pacman;

import java.awt.Color;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class GA {

    public int generation;
    public int pop, gx, gy;
    public int sx, sy;
    public BufferedWriter writer;
    public FileWriter filewriter;

    public GA(int sx, int sy) {
        this.sx = sx;
        this.sy = sy;
        this.generation = 0;
        this.pop = 0;
    }

    public void updatestart(int sx, int sy) {
        this.sx = sx;
        this.sy = sy;
    }

    public void saveBest(ArrayList<Player> pls) {

        Collections.sort(pls);
        Player p = pls.get(0);
        try {
            this.filewriter = new FileWriter("./Pacman/bestPlayer.txt", false);
            this.writer = new BufferedWriter(this.filewriter);

            writer.write(p.brain.weights_hi.rows + " " + p.brain.weights_hi.cols + " ");
            for (double t : p.brain.weights_hi.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(p.brain.weights_oh.rows + " " + p.brain.weights_oh.cols + " ");
            for (double t : p.brain.weights_oh.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(p.brain.bias_h.rows + " " + p.brain.bias_h.cols + " ");
            for (double t : p.brain.bias_h.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(p.brain.bias_o.rows + " " + p.brain.bias_o.cols + " ");
            for (double t : p.brain.bias_o.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(p.fitness + "");
            writer.close();
        } catch (IOException e) {
            System.out.println("Cannot write");
        }
    }

    public ArrayList<Player> nextGeneration(ArrayList<Player> sp, int p, int gx, int gy) {
        this.pop = p;
        this.gx = gx;
        this.gy = gy;

        ArrayList<Player> players = new ArrayList<Player>();
        //Collections.sort(sp);
        // System.out.println(sp.get(0).score+"---- "+sp.get(0).x+","+sp.get(0).y);
        // System.out.println(sp.get(199).fitness);
        int ma = 0;
        for(int i=0;i<sp.size();i++){
            if(sp.get(i).fitness>sp.get(ma).fitness){
                ma = i;
            }
        }
        sp.get(ma).color = new Color((int)Math.round(Math.random()*255),(int)Math.round(Math.random()*255),(int)Math.round(Math.random()*255));
        //System.out.println(sp.get(ma).fitness);
        for (int i = 0; i < this.pop; i++) {
            players.add(this.pickOne(sp));
        }
        // Player pl = new Player(sp.get(0), sx, sy, gx, gy);
        // pl.color = Color.YELLOW;
        // players.add(pl);
       
        // System.out.println("______________");
        sp.clear();
        this.generation++;
        return players;
    }

    public int getHighestScore(ArrayList<Player> sp) {
        int h = 0;
        for (int i = 0; i < sp.size(); i++) {
            if (sp.get(i).score > sp.get(h).score) {
                h = i;
            }
        }
        return h;
    }

    private Player pickOne(ArrayList<Player> sp) {
        double r = Math.random() * 1;
        int index = 0;
        int ma = 0;

        for(int i=0;i<sp.size();i++){
            if(sp.get(i).fitness>sp.get(ma).fitness){
                ma = i;
            }
        }

        while (r > 0 && index < sp.size()) {
            r = r - sp.get(index).fitness;
            index++;
        }

        if (index >= sp.size()) {
            index = ma;
            sp.get(ma).mutate(1);
        } else {
            index--;
        }

        Player player = new Player(sp.get(index), sx, sy, gx, gy);
        player.mutate();
        return player;
    }

    public void calculateFitness(ArrayList<Player> players) {
        int sum = 0;
        // double dis = distance(sx, sy, gx, gy);
        for (int i = 0; i < players.size(); i++) {
            sum += players.get(i).score;
        }
        for (int i = 0; i < players.size(); i++) {
            players.get(i).fitness = (double) (players.get(i).score / sum);
        
        }
    }

    public double distance(int x, int y, int x2, int y2) {
        int rise = Math.abs((y2 - y));
        int run = Math.abs((x2 - x));
        return Math.sqrt(Math.pow(rise, 2) + Math.pow(run, 2));
    }

}