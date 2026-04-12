#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    // Optimized isSafe: Since we fill row by row, 
    // we only need to check columns and diagonals ABOVE the current row.
    bool isSafe(vector<string> &board, int row, int col, int n) {
        // 1. Check Column (Above current row)
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }

        // 2. Check Left-Upward Diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }

        // 3. Check Right-Upward Diagonal
        for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') return false;
        }

        return true;
    }

    void nQueen(vector<string> &board, int row, int n, vector<vector<string>> &ans) {
        // Base Case: If we've reached beyond the last row, we found a solution
        if (row == n) {
            ans.push_back(board);
            return;
        }

        // Try placing a queen in every column of the current row
        for (int j = 0; j < n; j++) {
            if (isSafe(board, row, j, n)) {
                board[row][j] = 'Q';          // Place Queen
                nQueen(board, row + 1, n, ans); // Recur for next row
                board[row][j] = '.';          // Backtrack (Remove Queen)
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.')); 
        vector<vector<string>> ans;
        nQueen(board, 0, n, ans);
        return ans;
    }
};

int main() {
    int n;
    cout << "Enter the size of the board (N): ";
    cin >> n;

    Solution sol;
    vector<vector<string>> results = sol.solveNQueens(n);

    cout << "\nTotal solutions found: " << results.size() << "\n" << endl;

    for (int i = 0; i < results.size(); i++) {
        cout << "Solution " << i + 1 << ":" << endl;
        for (string row : results[i]) {
            cout << row << endl;
        }
        cout << "-------------------" << endl;
    }

    return 0;
}
