package FlappyBird;

//import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
// import java.io.IOException;
// import java.util.Random;

import javax.imageio.ImageIO;

public class Pipe {

    public int WIDTH = 400;
    public int HEIGHT = 600;

    public int top, bottom;
    public int x, w, speed, space;

    public boolean highlight;
    public Image pipe_top,pipe_bottom,pipe_top_body,pipe_bottom_body;

    public Pipe(){
        this.space = 80;
        // double[] r = {0.3,0.4,0.5};
        this.top = (int) Math.round(Math.random() * (HEIGHT - this.space) + 1);
        this.bottom = HEIGHT - this.space - top;
        this.x = WIDTH;
        this.w = 40;
        this.speed = 3;
        this.highlight = false;
        try{
            BufferedImage originalimage = ImageIO.read(new File("./FlappyBird/pipe_top.png"));
            this.pipe_top = originalimage.getScaledInstance(this.w, 20,java.awt.Image.SCALE_DEFAULT);
            originalimage = ImageIO.read(new File("./FlappyBird/pipe_bottom.png"));
            this.pipe_bottom = originalimage.getScaledInstance(this.w, 20,java.awt.Image.SCALE_DEFAULT);
            originalimage = ImageIO.read(new File("./FlappyBird/pipe_body.png"));
            this.pipe_top_body = originalimage.getScaledInstance(this.w, this.top,java.awt.Image.SCALE_DEFAULT);
            this.pipe_bottom_body = originalimage.getScaledInstance(this.w, this.bottom,java.awt.Image.SCALE_DEFAULT);
        }catch(Exception e){}
    }

    public void draw(Graphics g)
    {
        // if(this.highlight){
        //     g.setColor(Color.RED);
        // }
        // g.setColor(Color.WHITE);
        g.drawImage(pipe_bottom_body, this.x, HEIGHT - this.bottom,null);
        g.drawImage(pipe_bottom, this.x, HEIGHT - this.bottom-20,null);
        g.drawImage(pipe_top_body, this.x, 0,null);
        g.drawImage(pipe_top, this.x, this.top-20,null);
        // g.fillRect(this.x, 0, this.w, this.top);
        // g.fillRect(this.x, HEIGHT - this.bottom, this.w, this.bottom - 10);
    }

    public void update() {
        this.x -= this.speed;
    }

    public boolean hits(Bird bird) {
        if (bird.y < this.top || bird.y + bird.size > HEIGHT - this.bottom) {
            if ((bird.x + bird.size > this.x && bird.x + bird.size < this.x + this.w)
                    || (bird.x > this.x && bird.x < this.x + this.w)) {
                this.highlight = true;
                return true;
            }
        }
        return false;
    }

    public boolean offscreen() {
        return this.x < -this.w;
    }
}