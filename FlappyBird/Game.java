package FlappyBird;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

import java.awt.Image;

@SuppressWarnings("serial")
class Game extends JPanel implements Runnable, KeyListener {

    public int POP = 500;

    public int WIDTH = 400;
    public int HEIGHT = 600;

    public int FPS = 30;
    public long TargetTime = 1000 / FPS;

    public Thread thread;
    public boolean running;

    public Graphics2D g;
    public BufferedImage img;
    public Image flappybird,bg,bg_ground;

    public ArrayList<Bird> birds;
    public ArrayList<Bird> savedbirds;
    public ArrayList<Pipe> pipes;
    public int score, highscore;
    public boolean pipeclear;

    public int framecounter;
    public GA ga;
    public int cycle;
    public boolean best;

    public Game() {
        super();
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        this.setBackground(Color.BLACK);

        this.ga = new GA();
        this.birds = new ArrayList<Bird>();
        this.savedbirds = new ArrayList<Bird>();

        for (int i = 0; i < this.POP; i++) {
            this.birds.add(new Bird());
        }
        //this.birds.add(this.ga.getBestBird());
        try {
            BufferedImage originalimage = ImageIO.read(new File("./FlappyBird/bird.png"));
            this.flappybird = originalimage.getScaledInstance(this.birds.get(0).size,this.birds.get(0).size,java.awt.Image.SCALE_DEFAULT);
            originalimage = ImageIO.read(new File("./FlappyBird/flappy_bg.png"));
            this.bg = originalimage.getScaledInstance(WIDTH, HEIGHT, java.awt.Image.SCALE_DEFAULT);
            originalimage = ImageIO.read(new File("./FlappyBird/flappy_ground.png"));
            this.bg_ground = originalimage.getScaledInstance(WIDTH, 10, java.awt.Image.SCALE_DEFAULT);
        } catch (IOException e) {}
        this.pipes = new ArrayList<Pipe>();
        this.pipes.add(new Pipe());

        this.framecounter = 0;
        this.score = 0;
        this.highscore = 0;
        this.pipeclear = true;
        this.cycle = 1;
        this.best = false;
    }

    public void addNotify() {
        super.addNotify();
        if (this.thread == null) {
            this.thread = new Thread(this);
            this.addKeyListener(this);
            this.thread.start();
        }
        this.setFocusable(true);
        this.requestFocus();
        try {
            BufferedImage originalimage = ImageIO.read(new File("./FlappyBird/flappy_bg.png"));
            this.bg = originalimage.getScaledInstance(WIDTH, HEIGHT, java.awt.Image.SCALE_DEFAULT);
        } catch (IOException e) {}
    }

    public void init() {
        this.img = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
        this.g = (Graphics2D) img.getGraphics();
        this.running = true;

    }

    public void run() {
        init();
        long start, elsaped, wait;
        while (running) {
            start = System.nanoTime();

            draw();
            update();
            drawToScreen();

            elsaped = System.nanoTime() - start;

            wait = this.TargetTime - elsaped / 1000000;

            if (wait <= 0) {
                wait = 5;
            }

            try {
                Thread.sleep(wait);
            } catch (Exception e) {
                System.out.println("Problem with Game Loop");
            }

        }
    }

    public void draw() {
        g.drawImage(this.bg, 0,0,null);
        for (int t = 0; t < this.cycle; t++) {
            for (int a = 0; a < this.pipes.size(); a++) {
                pipes.get(a).update();

                if (this.birds.isEmpty()) {
                    this.score = 0;
                    this.framecounter = 0;
                    this.pipes.clear();
                    this.pipes.add(new Pipe());
                    this.birds = this.ga.nextGeneration(this.birds, this.savedbirds,this.POP,this.best);
                    break;
                }

                
                for (int i = 0; i < this.birds.size(); i++) {
                    if (pipes.get(a).hits(this.birds.get(i)) || this.birds.get(i).y<=0 || this.birds.get(i).y+this.birds.get(i).size>=HEIGHT-10) {
                        this.savedbirds.add(this.birds.get(i));
                        this.ga.calculateFitness(this.savedbirds);
                        this.birds.remove(i);
                    }
                }


                if (pipes.get(a).offscreen()) {
                    this.pipes.remove(0);
                    if(!this.birds.isEmpty()){
                        this.score++;
                    }
                    if (this.score > this.highscore) {
                        this.highscore = score;
                    }
                    this.pipeclear = true;
                    this.birds = this.ga.nextGeneration(this.birds, this.savedbirds,this.POP,this.best);
                }
            }
            for (Bird b : this.birds) {
                b.think(this.pipes);
                b.update();
            }
            this.framecounter++;

            if (this.framecounter % 100 == 0) {
                this.pipes.add(new Pipe());
            }
        }
        g.drawString("Score: " + this.score, 0, 20);
        g.drawString("Highscore: " + this.highscore, 0, 40);
        g.drawString("Generation: " + this.ga.generation, 0, 60);

        for (Pipe p : this.pipes) {
            p.draw(g);
        }
        for (Bird b : this.birds) {
            b.draw(g,this.flappybird);
        }
        g.drawImage(this.bg_ground, 0,HEIGHT-10,null);
    }

    public void drawToScreen() {
        Graphics g2 = getGraphics();
        g2.drawImage(img, 0, 0, null);
        g2.dispose();

        g.clearRect(0, 0, WIDTH, HEIGHT);
    }

    public void update() {}

    public void keyTyped(KeyEvent e) {}

    public void keyPressed(KeyEvent e) {
        // if (e.getKeyCode() == KeyEvent.VK_SPACE) {
        //     for(Bird b:this.birds){
        //         b.up();
        //     }
        // }
        if (e.getKeyCode() == KeyEvent.VK_L) {
            this.cycle = 100;
            System.out.println("Cycle at 100");
        }
        if (e.getKeyCode() == KeyEvent.VK_K) {
            this.cycle = 10;
            System.out.println("Cycle at 10");
        }
        if (e.getKeyCode() == KeyEvent.VK_J) {
            this.cycle = 1;
            System.out.println("Cycle at 1");
        }
        if (e.getKeyCode() == KeyEvent.VK_I) {
            this.cycle = 1;
            this.POP = 1;
            System.out.println("Population 1");
        }
        if (e.getKeyCode() == KeyEvent.VK_O) {
            this.cycle = 1;
            this.POP = 250;
            System.out.println("Population at 250");
        }
        if (e.getKeyCode() == KeyEvent.VK_P) {
            this.cycle = 1;
            this.POP = 500;
            System.out.println("Population at 500");
        }
        if (e.getKeyCode() == KeyEvent.VK_Q) {
            this.cycle = 1;
            this.POP = 0;
            this.best = true;
            System.out.println("Best Bird");
        }
        if (e.getKeyCode() == KeyEvent.VK_W) {
            this.cycle = 1;
            this.POP = 0;
            this.best = false;
            System.out.println("Normal");
        }
        if (e.getKeyCode() == KeyEvent.VK_S) {
            this.ga.saveBestBird(this.birds);
            System.out.println("Saved");
        }
        if (e.getKeyCode() == KeyEvent.VK_A) {
            this.birds.add(this.ga.bestBird);
            System.out.println("Big Bird");
        }
    }

    public void keyReleased(KeyEvent e) {}

    public static void main(String args[]) {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.add(new Game());
        frame.pack();
    }
}