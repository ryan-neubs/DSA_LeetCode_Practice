import java.util.HashSet;

public class validSudoku {

    public boolean validSudoku(char[][] board){
        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] col = new HashSet[9];
        HashSet<Character>[] boxes = new HashSet[9];
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){

                char num = board[i][j];
                if(num == '.'){
                    continue;
                }

                if(rows[i].contains(num)){
                    return false;
                }
                rows[i].add(num);

                if (col[j].contains(num)){
                    return false;
                }
                col[j].add(num);


                int boxIndex = (i/3) * 3 + (j/3);
                if(boxes[boxIndex].contains(num)){
                    return false;
                }
                boxes[boxIndex].add(num);
            }
        }
        return true;
    }


}
