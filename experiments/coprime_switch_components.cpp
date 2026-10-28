// Exact BFS of 4-cycle switches of coprime permutations.
// Build: g++ -O3 -std=c++17 experiments/coprime_switch_components.cpp -o coprime_switch
// Usage: ./coprime_switch 14
// For n=14, the search can use >200 MB RAM.
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
  int n = argc > 1 ? atoi(argv[1]) : 10;
  if (n < 1 || n > 14) { cerr << "Expected 1 <= n <= 14\n"; return 2; }
  // Independent total counts from OEIS A005326.
  const uint64_t known[15] = {0,1,1,3,4,28,16,256,324,3600,3600,129744,63504,3521232,3459600};
  bool coprime[15][15] = {};
  for (int i = 1; i <= n; ++i)
    for (int j = 1; j <= n; ++j)
      coprime[i][j] = gcd(i, j) == 1;

  // Cyclic shift: sigma(i)=i+1 for i<n; sigma(n)=1.
  // Each value is stored as a four-bit integer, encoded as value-1.
  uint64_t initial = 0;
  for (int i = 0; i < n; ++i)
    initial |= uint64_t((i + 1) % n) << (4 * i);

  vector<uint64_t> queue;
  queue.reserve(known[n]);
  queue.push_back(initial);
  unordered_set<uint64_t> visited;
  visited.reserve(known[n] * 1.3);
  visited.insert(initial);

  for (size_t front = 0; front < queue.size(); ++front) {
    uint64_t state = queue[front];
    for (int i = 0; i < n; ++i) {
      int x = int((state >> (4 * i)) & 15) + 1;
      for (int j = i + 1; j < n; ++j) {
        int y = int((state >> (4 * j)) & 15) + 1;
        if (!coprime[i + 1][y] || !coprime[j + 1][x]) continue;
        uint64_t mask = (uint64_t((x-1)^(y-1)) << (4*i)) |
                        (uint64_t((x-1)^(y-1)) << (4*j));
        uint64_t next = state ^ mask;
        if (visited.insert(next).second) queue.push_back(next);
      }
    }
  }
  cout << "n=" << n << " component_size=" << queue.size()
       << " total_known_permutations=" << known[n]
       << " connected=" << (queue.size() == known[n] ? "yes" : "not_verified") << '\n';
  return 0;
}
