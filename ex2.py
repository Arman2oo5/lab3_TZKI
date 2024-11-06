def display_grid(text, num_rows):
    
    num_cols = (len(text) + num_rows - 1) // num_rows  
    
    grid = [["" for _ in range(num_cols)] for _ in range(num_rows)]
    index = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    print("Кесте:")
    for row in grid:
        print(" | ".join(char if char else " " for char in row))
    
    return grid

def encrypt(grid, num_rows):
    
    encrypted_text = ''.join([grid[row][col] if grid[row][col] != "" else " " for col in range(len(grid[0])) for row in range(num_rows)])
    return encrypted_text

def decrypt(encrypted_text, num_rows, original_length):
 
    num_cols = (len(encrypted_text) + num_rows - 1) // num_rows  
    grid = [["" for _ in range(num_cols)] for _ in range(num_rows)]
    
    index = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if index < len(encrypted_text):
                grid[row][col] = encrypted_text[index]
                index += 1
    
   
    decrypted_text = ''.join([grid[row][col] if grid[row][col] != "" else " " for row in range(num_rows) for col in range(num_cols)])
    
    decrypted_text = decrypted_text[:original_length]
    return decrypted_text

text = input("Мәтінді енгізіңіз: ")
num_rows = int(input("Жолдар санын енгізіңіз: "))

original_length = len(text)

grid = display_grid(text, num_rows)


encrypted_text = encrypt(grid, num_rows)
print(f"\nДешифрленген текст: {encrypted_text}")


decrypted_text = decrypt(encrypted_text, num_rows, original_length)
print(f"\nШифрленген текст: {decrypted_text}")


