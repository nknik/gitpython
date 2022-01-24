#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the insertionSort1 function below.
void insertionSort1(int n, vector<int> arr)
{
    //int i,j,temp,;
    int small, sorted = 1, position, i, j, temp;
    /*for (int i = 0; i< n; i++)
{
    if (arr[i] > arr[i+1])
    {
        small = arr[i+1]; 
        position = i; 
        break; 
    }
    print();
}*/
    for (int i = n - 1; i > 0; i--)
    {
        for (j = i - 1; j >= 0; j--)
        {
            if (arr[j] > arr[i])
            {
                temp = arr[i];
                arr[i] = arr[j];
                for (int k = 0; k < n; k++)
                {
                    printf("%d ", arr[k]);
                }
                arr[j] = temp;
                printf("\n");
            }
        }
    }

    for (int k = 0; k < n; k++)
    {
        printf("%d ", arr[k]);
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    insertionSort1(n, arr);

    return 0;
}

vector<string> split_string(string input_string)
{
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ')
    {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos)
    {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
// Input (stdin)

// Download
// 5
// 2 4 6 8 3
// Expected Output

// Download
// 2 4 6 8 8
// 2 4 6 6 8
// 2 4 4 6 8
// 2 3 4 6 8