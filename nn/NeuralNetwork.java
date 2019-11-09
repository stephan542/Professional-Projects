package nn;

import java.util.Random;

public class NeuralNetwork {

    public int input_nodes, hidden_nodes, output_nodes;
    public Matrix weights_hi, weights_oh, bias_h, bias_o;
    public double learning_rate;

    public NeuralNetwork(NeuralNetwork nn){
        this.learning_rate = 0.1;
        this.input_nodes = nn.input_nodes;
        this.hidden_nodes = nn.hidden_nodes;
        this.output_nodes = nn.output_nodes;

        this.weights_hi = nn.weights_hi.copy();
        this.weights_oh = nn.weights_oh.copy();

        this.bias_h = nn.bias_h.copy();
        this.bias_o = nn.bias_o.copy();
    }
    public NeuralNetwork(int a, int b, int c) {

        this.learning_rate = 0.1;
        this.input_nodes = a;
        this.hidden_nodes = b;
        this.output_nodes = c;

        this.weights_hi = new Matrix(this.hidden_nodes, this.input_nodes);
        this.weights_oh = new Matrix(this.output_nodes, this.hidden_nodes);

        this.weights_hi.randomize();
        this.weights_oh.randomize();

        this.bias_h = new Matrix(this.hidden_nodes, 1);
        this.bias_o = new Matrix(this.output_nodes, 1);

        this.bias_h.randomize();
        this.bias_o.randomize();
    }

    
    public double[] predict(double[] k) {
        Matrix inputs = new Matrix().fromArray(k);
        Matrix hidden = new Matrix().multiply(this.weights_hi, inputs);
        hidden.add(this.bias_h);
        for (int i = 0; i < hidden.rows; i++) {
            for (int j = 0; j < hidden.cols; j++) {
                hidden.data[i][j] = this.sigmoid(hidden.data[i][j], true);
            }
        }

        Matrix output = new Matrix().multiply(this.weights_oh, hidden);
        output.add(this.bias_o);

        for (int i = 0; i < output.rows; i++) {
            for (int j = 0; j < output.cols; j++) {
                output.data[i][j] = this.sigmoid(output.data[i][j], true);
            }
        }
        return output.toarray();

    }

    public double sigmoid(double x, boolean f) {
        if (f) {
            return 1 / (1 + Math.exp(-x));
        } else {
            return x * (1 - x);
        }
    }

    public double tanh(double x, boolean f) {
        if (f) {
            return Math.tanh(x);
        } else {
            return 1 - (x * x);
        }
    }

    public NeuralNetwork copy() {
        return new NeuralNetwork(this);
    }

    public void mutate(double u) {
        for (int i = 0; i < this.weights_hi.rows; i++) {
            for (int j = 0; j < this.weights_hi.cols; j++) {
                if(Math.random() < u){
                    this.weights_hi.data[i][j] += new Random().nextGaussian()*0.1;
                }
            }
        }
        for (int i = 0; i < this.weights_oh.rows; i++) {
            for (int j = 0; j < this.weights_oh.cols; j++) {
                if(Math.random() < u){
                    this.weights_oh.data[i][j] += new Random().nextGaussian()*0.1;
                }
            }
        }
        for (int i = 0; i < this.bias_h.rows; i++) {
            for (int j = 0; j < this.bias_h.cols; j++) {
                if(Math.random() < u){
                    this.bias_h.data[i][j] += new Random().nextGaussian()*0.1;
                }
            }
        }
        for (int i = 0; i < this.bias_o.rows; i++) {
            for (int j = 0; j < this.bias_o.cols; j++) {
                if(Math.random() < u){
                    this.bias_o.data[i][j] += new Random().nextGaussian()*0.1;
                }
            }
        }
    }

    public String toString(){
        return this.bias_o.toString();
    }

    // public static void main(String[] args) {
    //     NeuralNetwork nn = new NeuralNetwork(4, 4, 1);
    //     System.out.println(nn.bias_h);
    //     NeuralNetwork nn2 = nn.copy();
    //     System.out.println(nn.bias_h);
    // }
}