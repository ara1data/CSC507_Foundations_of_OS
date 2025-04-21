# Module 4 Critical Thinking Assignment
# First-Fit Algorithm Simulations

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC507-1: Foundations of Operating Systems
# Dr. Joseph Issa
# April 13, 2025

# ------------------------------

# First-Fit Algorithm Function
def first_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i, process in enumerate(process_sizes):
        for j, block in enumerate(block_sizes):
            if block >= process:
                allocation[i] = j
                block_sizes[j] -= process
                break
    return allocation

# ---------- Predefined Values ----------
# Blocks of Memory
blocks = [100, 500, 200, 300, 600]
# Process Memory Requirements
processes = [212, 417, 112, 426]

# ---------- Execute the First-Fit Algorithm Function ----------
# Store results in the "results" variable
result = first_fit(blocks.copy(), processes)

# ---------- Print results in the terminal ----------
print("Process No.\tProcess Size\tBlock No.")
# Structure output in table format
for idx, alloc in enumerate(result):
    print(f"{idx+1}\t\t{processes[idx]}\t\t{alloc+1 if alloc != -1 else 'Not Allocated'}")
