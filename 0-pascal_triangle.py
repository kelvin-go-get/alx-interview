def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1s
        # Fill the row excluding the first and last element
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


# Example usage
if __name__ == "__main__":

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join(map(str, row))))

    # Test case with n = 5
    print_triangle(pascal_triangle(5))
