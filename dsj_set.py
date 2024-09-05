class DisjointSet:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0 for x in range (n)]

    def find(self, i):
        if (i != self.parent[i]):
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        i_id = self.find(self.parent[i])
        j_id = self.find(self.parent[j])
        if (j_id == i_id):
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1

def test_disjoint_set():
    # Create a DisjointSet with 10 elements
    ds = DisjointSet(10)
    
    # Perform some union operations
    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(5, 6)
    ds.union(7, 8)
    
    # Test find operations
    assert ds.find(1) == ds.find(3), "Test failed: 1 and 3 should be in the same set"
    assert ds.find(4) == ds.find(6), "Test failed: 4 and 6 should be in the same set"
    assert ds.find(7) == ds.find(8), "Test failed: 7 and 8 should be in the same set"
    
    # Test that different sets are not connected
    assert ds.find(1) != ds.find(4), "Test failed: 1 and 4 should be in different sets"
    assert ds.find(2) != ds.find(5), "Test failed: 2 and 5 should be in different sets"
    
    # More union operations to connect sets
    ds.union(3, 4)
    
    # Test after connecting two sets
    assert ds.find(1) == ds.find(5), "Test failed: 1 and 5 should now be in the same set after union(3, 4)"
    
    # Print success message if all tests pass
    print("All tests passed!")

# Run the test
#test_disjoint_set()