class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        // quick sort
        int m = mat.size(), n = mat[0].size();

        function<int(int, int, int, int, int)> partition = [&](int x, int y, int dx, int dy, int len) -> int {
            int pi = mat[x + (len - 1) * dx][y + (len - 1) * dy];
            int i = -1;
        
            for (int j = 0; j < len - 1; ++j) {
                int cx = x + j * dx, cy = y + j * dy;
                if (mat[cx][cy] < pi) {
                    ++i;
                    swap(mat[x + i * dx][y + i * dy], mat[cx][cy]);
                }
            }
            swap(mat[x + (i + 1) * dx][y + (i + 1) * dy], mat[x + (len - 1) * dx][y + (len - 1) * dy]);
            return i + 1; 
        };

        function<void(int, int, int, int, int, int)> quick = [&](int x, int y, int dx, int dy, int l, int h) {
            if (l < h) {
                int pi = partition(x + l * dx, y + l * dy, dx, dy, h - l + 1);
                quick(x, y, dx, dy, l, l + pi - 1);
                quick(x, y, dx, dy, l + pi + 1, h);
            }
        };

        // start first row
        for (int i = 0; i < n; ++i) {
            int length = min(m, n - i);
            quick(0, i, 1, 1, 0, length - 1);
        }

        // start first col
        for (int i = 1; i < m; ++i) {
            int length = min(n, m - i);
            quick(i, 0, 1, 1, 0, length - 1);
        }

        return mat;
    }
};
