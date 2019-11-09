package nn;

public class Matrix {

    public int rows, cols;
    public double data[][];

    public Matrix() {
        this.rows = 0;
        this.cols = 0;
    }

    public void add(Matrix b) {
        if (this.rows == b.rows && this.cols == b.cols) {
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    this.data[i][j] += b.data[i][j];
                }
            }
        }
    }

    public Matrix copy(){
        Matrix m = new Matrix(this.rows,this.cols);
        for (int i = 0; i < this.rows; i++) {
            for (int j = 0; j < this.cols; j++) {
                m.data[i][j] = this.data[i][j];
            }
        }
        return m;
    }

    public double[] toarray() {
        double[] arr = new double[this.cols * this.rows];
        int count = 0;
        for (int i = 0; i < this.rows; i++) {
            for (int j = 0; j < this.cols; j++) {
                arr[count]=this.data[i][j];
                count++;
            }
        }
        return arr;
    }

    public Matrix(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;

        this.data = new double[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                this.data[i][j] = 0;
            }
        }
    }

    public Matrix fromArrayMatrix(double[] arr){
        Matrix newm = new Matrix((int)Math.round(arr[0]),(int)Math.round(arr[1]));
        int count = 2;
        for (int i = 0; i < newm.rows; i++) {
            for (int j = 0; j < newm.cols; j++) {
                newm.data[i][j] = (double)arr[count];
                count++;
            }
        }
        return newm;
    }

    public Matrix fromArray(double[] arr) {
        Matrix m = new Matrix(arr.length, 1);
        for (int i = 0; i < arr.length; i++) {
            m.data[i][0] = arr[i];
        }
        return m;
    }

    public void randomize() {
        for (int i = 0; i < this.rows; i++) {
            for (int j = 0; j < this.cols; j++) {
                this.data[i][j] = Math.random() * 2 - 1;
            }
        }
    }

    public Matrix multiply(Matrix a, Matrix b) {
        if (a.cols == b.rows) {
            Matrix newmatrix = new Matrix(a.rows, b.cols);
            double[] bcol = new double[b.rows];
            for (int i = 0; i < newmatrix.rows; i++) {
                for (int j = 0; j < newmatrix.cols; j++) {
                    for (int k = 0; k < b.rows; k++) {
                        bcol[k] = b.data[k][j];
                    }
                    newmatrix.data[i][j] = this.multiplyArray(a.data[i], bcol);
                }
            }
            return newmatrix;
        }
        return null;
    }

    public double multiplyArray(double[] a, double[] b) {
        double sum = 0;
        for (int i = 0; i < a.length; i++) {
            sum += a[i] * b[i];
        }
        return sum;

    }

    public String toString() {
        String output = "";
        for (int i = 0; i < this.rows; i++) {
            for (int j = 0; j < this.cols; j++) {
                output += this.data[i][j] + " ";
            }
            output += "\n";
        }
        return output;
    }
}