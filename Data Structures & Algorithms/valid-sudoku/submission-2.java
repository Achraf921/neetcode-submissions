class Solution {
    public boolean isValidSudoku(char[][] board) {
        //brute-force : check every row->column->3x3
        //time complexity : O(n^3)
        //an improved solution
        //HashMap/     Array[9] for counting
        /*
        column 1 : [1,0,0,1,1,0,1,0,0]
        column 2 : [0,1,0,0,0,0,0,0,1]
        
        rows 1 : [col1[1]+col2[1]+col3[1],]
        */
        //Actually I'll use a hashset to check row->col->box
    
    //checking rows (easiest)
    for(char[] row : board){
        HashSet<Character> hset = new HashSet<>();
        for(char num: row){
            if(!(Character.isDigit(num)||num=='.'))
                return false;
            else if(hset.contains(num))
                return false;
            else if(num!='.')
                hset.add(num);
        }
    }
    //checking collumns (a bit more difficult)
    for(int i=0;i<9;i++){
        HashSet<Character> hset = new HashSet<>();
        for(char[] row : board){
            if(!(Character.isDigit(row[i])||row[i]=='.'))
                return false;
            else if(hset.contains(row[i]))
                return false;
            else if(row[i]!='.')
                hset.add(row[i]);
        }
    }
    //checking boxes (most difficult out of the 3)
    for(int i=0;i<3;i++){//iterates over our 3 rows of boxes
        for(int k=0;k<3;k++){//iterates over our 3 collumn of boxes
        HashSet<Character> hset= new HashSet<>();//box specific hashSet
            for(int c=k*3;c<k*3+3;c++){//col
                for(int j=i*3;j<i*3+3;j++){//row
                    if(!(Character.isDigit(board[j][c])||board[j][c]=='.'))
                        return false;
                    else if(hset.contains(board[j][c]))
                        return false;
                    else if(board[j][c]!='.')
                        hset.add(board[j][c]);
                }
            }

        }
    }
    return true;
}
}
