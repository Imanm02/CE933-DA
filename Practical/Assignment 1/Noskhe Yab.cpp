#include <iostream>
#include <vector>
#include<math.h>

using namespace std;

int main() {
    int allChocoloates, allDays;

    scanf("%d%d", &allChocoloates, &allDays);

    vector<uint32_t> bNumber(allChocoloates, pow(2,30)-1);
    vector<vector<pair<uint32_t, uint32_t>>> pairs(allChocoloates);

    for (int i = 0; i < allDays; i++) {

        uint32_t day1;
        uint32_t day2;
        uint32_t day3;
        uint32_t day4;
        uint32_t day5;

        cin >> day1;
        cin >> day2;
        cin >> day3;

        day1 = day1 - 1;
        day2 = day2 - 1;

        pairs[day1].emplace_back(day2, day3);
        pairs[day2].emplace_back(day1, day3);

        day1 = day1 + 1;
        day2 = day2 + 1;
        
        if (day1 > day2){
            day4 = day1;
            day1 = day2;
            day2 = day4; 
        }

    }

    for (int i = 1; i <= 30; ++i) {
        for (int j = 1; j <= allChocoloates; ++j) { 
            for (int k = 1; k <= pairs[j-1].size(); k++) {
                if (!(((pairs[j-1][k-1].second) >> i-1) & 1))
                    bNumber[j-1] = bNumber[j-1] & (~(1 << i-1));
            }
        }

        for (int j = 0; j < allChocoloates; ++j) {
            if ((bNumber[j] >> i-1) & 1) {
                bNumber[j] = bNumber[j] & (~(1 << i-1));
                for (int k = 0; k < pairs[j].size(); k++) {
                    if ((((pairs[j][k].second) >> i-1) & 1) && !((bNumber[pairs[j][k].first] >> i-1) & 1)) {
                        bNumber[j] = bNumber[j] | (1 << i-1);
                        break;
                    }
                }
            }
        }
    }

    for (int i = 0; i < allChocoloates; ++i) {
        printf("%d ", bNumber[i]);
    }
}