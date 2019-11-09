window.onload = function () {

    var board = document.getElementById("board").children;
    var status = "X";

    document.querySelector('.btn').addEventListener("click", function () {
        for (var i = 0; i < board.length; i++) {
            board[i].setAttribute("class","square");
            board[i].addEventListener("click",clickevent);
            board[i].innerHTML = "";
            document.getElementById("status").innerHTML = "Move your mouse over a square and click to play an X or an O";
            document.getElementById("status").classList.remove("you-won");
            status = "X";

        }
    })

    for (var i = 0; i < board.length; i++) {
        board[i].addEventListener("mouseover", function () {
            this.classList.add("hover");
            if(winnercheck(board)){
                this.removeEventListener("click",clickevent);
            }
            
        });
        board[i].addEventListener("mouseout", function () {
            this.classList.remove("hover");
        });
    }

    function clickevent(){
            if (!this.classList.contains("X") && !this.classList.contains("O")) {
                this.innerHTML = status;
                this.classList.add(status);
                if(winnercheck(board)){
                    document.getElementById("status").innerHTML = "Congratulations! "+status+" is the Winner!";
                    document.getElementById("status").classList.add("you-won");
                }
                if (status == "X") {
                    status = "O";
                } else {
                    status = "X";
                }
            }
    }
}

function winnercheck(b) {
    var brd = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]];
    var count = 0;
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (b[count].classList.contains("X")) {
                brd[i][j] = 1;
            } else if (b[count].classList.contains("O")){
                brd[i][j] = 10;
            }
            count++;
        }
    }

    for (var i = 0; i < 3; i++) {
        if (sum(brd[i]) == 30 || sum(brd[i]) == 3) {
            return true;
        }
    }

    for (var i = 0; i < 3; i++) {
        if (sum(vertical(brd, i)) == 30 || sum(vertical(brd, i)) == 3) {
            return true;
        }
    }

    for (var i = 0; i < 2; i++) {
        if (sum(diagonal(brd, i)) == 30 || sum(diagonal(brd, i)) == 3) {
            return true;
        }
    }

    return false;
}
function vertical(a, i) {
    return [a[0][i], a[1][i], a[2][i]]
}
function diagonal(a, b) {
    if (b == 0) {
        return [a[0][0], a[1][1], a[2][2]]
    } else {
        return [a[0][2], a[1][1], a[2][0]]
    }
}
function sum(a) {
    var ans = 0;
    for (var i = 0; i < a.length; i++) {
        ans += a[i];
    }
    return ans;
}

function get_valid_plays(){
  
}

function minimax(board,depth,aplha,beta,maxmizePlayer){
    if(maxmizePlayer){
        
    }

}