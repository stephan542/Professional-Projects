
package FlappyBird;

import nn.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class GA {

    public int generation;
    public int POP;
    public Bird bestBird;
    public Scanner scanner;
    public FileWriter filewriter;
    public BufferedWriter writer;

    public GA() {

        this.generation = 0;
        this.bestBird = getBestBird();

    }

    public Bird getBestBird() {
        try {
            scanner = new Scanner(new File("./FlappyBird/bestBird.txt"));
            NeuralNetwork nn = new NeuralNetwork(6, 8, 2);

            Matrix[] attr = { nn.weights_hi, nn.weights_oh, nn.bias_h, nn.bias_o };
            String w;
            double[] w1;
            int r, c, count, attricount;
            double fitness = 0;

            attricount = 0;
            while (scanner.hasNext()) {
                w = scanner.nextLine();

                if (w.split(" ").length == 1) {
                    fitness = Double.parseDouble(w);
                } else {
                    r = Integer.parseInt(w.split(" ")[0]);
                    c = Integer.parseInt(w.split(" ")[1]);
                    w1 = new double[r * c + 2];
                    count = 0;
                    for (int h = 0; h < (r * c) + 2; h++) {
                        w1[count] = Double.parseDouble(w.split(" ")[h]);
                        count++;
                    }

                    attr[attricount] = new Matrix().fromArrayMatrix(w1);
                    attricount++;
                }
            }

            nn.weights_hi = attr[0].copy();
            nn.weights_oh = attr[1].copy();
            nn.bias_h = attr[2].copy();
            nn.bias_o = attr[3].copy();

            this.bestBird = new Bird(nn);
            // System.out.println(this.bestBird.brain.weights_hi);
            // System.out.println(this.bestBird.brain.weights_oh);
            // System.out.println(this.bestBird.brain.bias_h);
            // System.out.println(this.bestBird.brain.bias_o);
            this.bestBird.fitness = fitness;
            return this.bestBird;
        } catch (FileNotFoundException e) {
            return null;
        }

    }

    public void saveBestBird(ArrayList<Bird> sb) {
        double score = 0;
        
        for(Bird b:sb){
            if(b.score>score){
                this.bestBird = b;
                score = b.score;
            }
        }
        
        try {
            this.filewriter = new FileWriter("./FlappyBird/bestBird.txt", false);
            this.writer = new BufferedWriter(this.filewriter);

            writer.write(bestBird.brain.weights_hi.rows + " " + bestBird.brain.weights_hi.cols + " ");
            for (double t : bestBird.brain.weights_hi.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(bestBird.brain.weights_oh.rows + " " + bestBird.brain.weights_oh.cols + " ");
            for (double t : bestBird.brain.weights_oh.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(bestBird.brain.bias_h.rows + " " + bestBird.brain.bias_h.cols + " ");
            for (double t : bestBird.brain.bias_h.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(bestBird.brain.bias_o.rows + " " + bestBird.brain.bias_o.cols + " ");
            for (double t : bestBird.brain.bias_o.toarray()) {
                writer.write(t + " ");
            }
            writer.newLine();
            writer.write(bestBird.fitness + "");
            writer.close();
        } catch (IOException e) {
            System.out.println("Cannot write");
        }
    }

    public ArrayList<Bird> nextGeneration(ArrayList<Bird> b, ArrayList<Bird> sb, int pop, boolean best) {
        ArrayList<Bird> birds = new ArrayList<Bird>();
        this.POP = pop;
        if (best) {
            birds.add(this.bestBird);
        }
        if (b.isEmpty()) {
            calculateFitness(b);
            for (int i = 0; i < this.POP; i++) {
                birds.add(this.pickOne(sb));
            }
            sb.clear();
            this.generation++;

            return birds;
        } else {
            return b;
        }
    }

    public Bird pickOne(ArrayList<Bird> sb) {
        int index = 0;
        double r = Math.random() * 1;

        while (r > 0) {
            r = r - sb.get(index).fitness;
            index++;
        }
        index--;

        Bird bird = sb.get(index);
        Bird child = new Bird(bird.brain);

        child.mutate();

        return child;
    }

    public void calculateFitness(ArrayList<Bird> b) {
        int sum = 0;
        for (Bird bd : b) {
            sum += bd.score;
        }
        for (Bird bd : b) {
            bd.fitness = (double) bd.score / sum;
        }
    }
}