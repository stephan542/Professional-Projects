package Pacman;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;

import java.awt.image.BufferedImage;
import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.awt.Graphics2D;
import java.awt.Graphics;

@SuppressWarnings("serial")
public class Game extends JPanel implements Runnable, KeyListener, MouseListener {

    public int WIDTH = 623;
    public int HEIGHT = 690;
    public int POP = 250;
    public long timer;

    public int DesiredFPS = 60;
    public long FPS = 0;
    public double TargetTime = 1000 / DesiredFPS;
    public boolean running = false;

    public Thread thread;
    public BufferedImage img, map;
    public Graphics2D g;

    public HashMap<String, Wall> walls;
    public ArrayList<Player> players;
    public GA ga;

    public int goalx = 31;
    public int goaly = 625;
    public int limit = 22000;
    public int startx = 32;
    public int starty = 31;
    public int[] goalsx = {31,560,31,559};
    public int[] goalsy = {31,163,625,427};

    public Game() {
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        this.setBackground(Color.black);
        this.thread = null;

        this.walls = new HashMap<String, Wall>();
        this.map = this.getMap("./Pacman/map.jpg");
        this.players = new ArrayList<Player>();
        this.ga = new GA(startx, starty);

        for (int i = 0; i < this.POP; i++) {
            this.players.add(new Player(startx,starty, this.walls, goalx, goaly));
        }

    }

    public void addNotify() {
        super.addNotify();
        if (this.thread == null) {
            this.thread = new Thread(this);
            this.addKeyListener(this);
            this.addMouseListener(this);
            this.thread.start();
        }
        this.running = true;
        this.requestFocus();
    }

    public void init() {
        this.img = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_ARGB);
        this.g = (Graphics2D) img.getGraphics();
        this.timer = System.currentTimeMillis();
    }

    public void run() {
        long start, elapsed, wait;
        init();
        while (this.running) {
            start = System.nanoTime();

            draw();
            drawToScreen();

            elapsed = System.nanoTime() - start;
            wait = (long) (TargetTime - (double) (elapsed / 1000000));

            this.FPS = (long) Math.round(elapsed / 1000000);
            if (wait < 0) {
                wait = 5;
            }

            try {
                Thread.sleep(wait);
            } catch (Exception e) {
                System.out.println("Problem with sleep thread");
            }

        }

    }

    public void draw() {
        g.drawImage(map, 0, 0, null);

        update();

        for (int i = 0; i < this.players.size(); i++) {
            this.players.get(i).draw(g);
        }
        g.setColor(Color.GREEN);
        g.drawRect(goalx, goaly, 29, 29);

        g.setColor(Color.RED);
        g.drawString("FPS:" + this.FPS, 10, 10);
        g.drawString("Generation: " + this.ga.generation, 10, 20);
    }

    public void update() {
        int r = (int) Math.round(Math.random()*2);

        for (int i = 0; i < this.players.size(); i++) {
            if(this.players.get(i).distance(this.goalx, this.goaly) <= 20){
                this.startx = this.goalx;
                this.starty = this.goaly;
                this.ga.updatestart(this.startx,this.starty);
                this.goalx = this.goalsx[r];
                this.goaly = this.goalsy[r];
                this.ga.calculateFitness(this.players);
                this.players = this.ga.nextGeneration(this.players, this.POP,this. goalx, this.goaly);
                this.timer = System.currentTimeMillis();
                break;
            }
        }

        for (int i = 0; i < this.players.size(); i++) {
            this.players.get(i).think(this.g);
            this.players.get(i).update();
        }

        if (System.currentTimeMillis() - this.timer >= this.limit) {
            this.ga.calculateFitness(this.players);
            this.players = this.ga.nextGeneration(this.players, this.POP, goalx, goaly);
            this.timer = System.currentTimeMillis();
        }
    }

    public void drawToScreen() {
        Graphics g2 = this.getGraphics();
        g2.drawImage(img, 0, 0, null);
        g2.dispose();

        g.clearRect(0, 0, WIDTH, HEIGHT);

    }

    public void keyPressed(KeyEvent e) {
        // if(e.getKeyCode() == KeyEvent.VK_UP){
        // this.players.get(0).up();
        // }
        // if(e.getKeyCode() == KeyEvent.VK_DOWN){
        // this.players.get(0).down();
        // }
        // if(e.getKeyCode() == KeyEvent.VK_LEFT){
        // this.players.get(0).left();
        // }
        // if(e.getKeyCode() == KeyEvent.VK_RIGHT){
        // this.players.get(0).right();
        // }
        if(e.getKeyCode() == KeyEvent.VK_S){
            System.out.println(this.players.get(0).brain.weights_hi);
            System.out.println(this.players.get(0).brain.weights_oh);
            System.out.println(this.players.get(0).brain.bias_h);
            System.out.println(this.players.get(0).brain.bias_o);
            
            this.ga.saveBest(this.players);
        }
        //if(e.getKeyCode() == KeyEvent.VK_RIGHT){
        //     this.players.get(0).right();
        // }
    }

    public void keyTyped(KeyEvent e) {
    }

    public void keyReleased(KeyEvent e) {
    }

    public BufferedImage getMap(String filename) {
        BufferedImage mapImage = null;
        int mapheight, mapwidth,a, r, g, b, c;
        long avg;
        try {
            mapImage = ImageIO.read(new File(filename));
        } catch (Exception e) {
            System.out.println("Cannot find map");
            System.exit(0);
        }
        mapheight = mapImage.getHeight();
        mapwidth = mapImage.getWidth();

        System.out.println(mapheight + " " + mapwidth);
        for (int i = 0; i < mapwidth; i++) {
            for (int j = 0; j < mapheight; j++) {
                c = mapImage.getRGB(i, j);
                a = (c >> 24) & 0xff;
                r = (c >> 16) & 0xff;
                g = (c >> 8) & 0xff;
                b = c & 0xff;
                avg = Math.round(0.2126 * r + 0.7152 * g + 0.0722 * b) + (a-a);
                // System.out.print(avg+" ");
                if (avg != 0) {
                    this.walls.put(i + "x" + j, new Wall(i, j));
                }
            }
        }
        return mapImage;
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.add(new Game());
        frame.pack();
    }

    public void mouseClicked(MouseEvent e) {
        System.out.println(this.walls.get(64+"x"+129));
        

    }
    public void mousePressed(MouseEvent e) {}public void mouseReleased(MouseEvent e) {}public void mouseEntered(MouseEvent e) {}public void mouseExited(MouseEvent e) {}
}