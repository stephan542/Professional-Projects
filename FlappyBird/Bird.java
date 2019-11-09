package FlappyBird;

import nn.*;
import java.awt.Image;

import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

public class Bird {

    public int WIDTH = 400;
    public int HEIGHT = 600;

    public int x, y;
    public int velocity;
    public int gravity;
    public int lift;
    public int size;
    public int score;
    public double fitness;
    public NeuralNetwork brain;
    public Color color;

    public Bird(NeuralNetwork brain) {
        this.intializeBird();
        this.brain = brain.copy();
    }

    public Bird() {
        this.intializeBird();
        this.brain = new NeuralNetwork(6, 8, 2);
        this.color = Color.WHITE;
    }

    public void intializeBird() {
        this.y = HEIGHT / 2;
        this.x = 25;
        this.velocity = 0;
        this.gravity = 1;
        this.lift = -20;
        this.size = 25;
        this.fitness = 0;
        this.score = 0;
        
    }
    public void think(ArrayList<Pipe> pipes) {
            Pipe closest = pipes.get(0);
            double closestD = this.x - closest.x;
            double d = Double.POSITIVE_INFINITY;
            for(Pipe p:pipes){
                d = (p.x + p.w) - this.x;
                
                if( d < closestD && d>0){
                    closest = p;
                    closestD = d;
                }
            }

            double[] inputs = new double[6];
            inputs[0] = (double) this.y / HEIGHT;
            inputs[1] = (double) closest.top / HEIGHT;
            inputs[2] = (double) closest.bottom / HEIGHT;
            inputs[3] = (double) closest.x / WIDTH;
            inputs[4] = (double) this.velocity/10;
            inputs[5] = (double) closest.w /10;

            
            double[] output = this.brain.predict(inputs);
            if (output[0] > output[1]) {
                this.up();
            }
    }

    public void increScore(int s) {
        this.score = s;
    }

    public void draw(Graphics g,Image flappybird) {
        // g.setColor(this.color);
        // g.fillOval(this.x, this.y, this.size, this.size);
        g.drawImage(flappybird, this.x,this.y,null);
    }

    public void up() {
        this.velocity += lift;
    }

    public void mutate(){
        this.brain.mutate(0.1);
    }

    public void update() {
        this.score++;
        this.velocity += (int) Math.round(gravity * 2);
        this.velocity = (int) Math.round(this.velocity * 0.9);
        this.y += velocity;

        if (this.y >= HEIGHT - this.size) {
            this.y = HEIGHT - this.size;
            this.velocity = 0;
        }
        if (this.y <= 0) {
            this.y = 0;
            this.velocity = 0;
        }
    }

}