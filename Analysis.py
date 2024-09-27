import timeit
import matplotlib.pyplot as plt
from Database_Operations import fetch_public_key_indexes, fetch_private_key_indexes
from modified_Version_RSA import encrypt as modified_encrypt, decrypt as modified_decrypt
from Traditional_RSA import generate_key_pair, encrypt as traditional_encrypt, decrypt as traditional_decrypt

# Benchmark for the first implementation (Traditional RSA)
def benchmark_first_implementation(message):
    # Time key generation
    start_time = timeit.default_timer()

    public, private = generate_key_pair()
    key_gen_time = timeit.default_timer() - start_time

    # Time encryption and decryption
    start_time = timeit.default_timer()
    encrypted = traditional_encrypt(public, message)
    decryption_time = timeit.default_timer() - start_time

    return key_gen_time, decryption_time, encrypted, private

# Benchmark for the second implementation (Modified RSA with database key fetching)
def benchmark_second_implementation_with_db_timing(message):
    start_time = timeit.default_timer()

    # Time key fetching from database
    publicKey = fetch_public_key_indexes()
    privateKey = fetch_private_key_indexes()
    fetch_time = timeit.default_timer() - start_time

    # Time encryption and decryption
    encrypted = modified_encrypt(publicKey, message)
    decryption_time = timeit.default_timer() - start_time - fetch_time

    return encrypted, privateKey, fetch_time, decryption_time

# Messages of different sizes for analysis
small_message = "Hello"
medium_message = "Life is short, so enjoy it!" * 10
large_message = "This is a large message. " * 100

messages = [small_message, medium_message, large_message]
message_sizes = ['Small', 'Medium', 'Large']

# Time both implementations for different message sizes
traditional_times = []
modified_times = []
fetch_times = []
encryption_decryption_times = []
traditional_key_gen_times = []
traditional_decryption_times = []

for message in messages:
    # Time the traditional implementation
    key_gen_time, decryption_time, encrypted, private = benchmark_first_implementation(message)
    traditional_total_time = key_gen_time + decryption_time
    traditional_times.append(traditional_total_time)
    traditional_key_gen_times.append(key_gen_time)
    traditional_decryption_times.append(decryption_time)

    # Time the modified implementation (including key fetching)
    _, privateKey, fetch_time, modified_decryption_time = benchmark_second_implementation_with_db_timing(message)
    fetch_times.append(fetch_time)
    encryption_decryption_time = modified_decryption_time
    modified_times.append(fetch_time + encryption_decryption_time)

plt.figure(figsize=(8, 6))

# Bar plot for traditional and modified implementation times
bar_width = 0.35
index = range(len(message_sizes))

plt.bar(index, traditional_times, bar_width, color='#1f77b4', label='Traditional RSA Total Time')
plt.bar([i + bar_width for i in index], modified_times, bar_width, color='#ff7f0e', label='Modified RSA Total Time')
plt.xlabel('Message Size')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison of RSA Implementations')
plt.xticks([i + bar_width / 2 for i in index], message_sizes)
plt.legend()

plt.tight_layout()
plt.show()

# Print results for reference
for i, size in enumerate(message_sizes):
    print(f"{size} Message:")
    print(f"  Traditional RSA Total Time: {traditional_times[i]:.6f} seconds")
    print(f"  Modified RSA Total Time: {modified_times[i]:.6f} seconds")
    print()