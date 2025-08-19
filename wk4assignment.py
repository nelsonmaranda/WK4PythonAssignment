
def read_file(filename):
    """Read a file and return its content."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"✅ Successfully read '{filename}'")
            return content
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"❌ Error: No permission to read '{filename}'")
        return None

def write_file(filename, content):
    """Write content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"✅ Successfully wrote to '{filename}'")
            return True
    except PermissionError:
        print(f"❌ Error: No permission to write '{filename}'")
        return False

def process_content(content):
    """Add line numbers to the content."""
    lines = content.split('\n')
    processed_lines = []
    
    for i, line in enumerate(lines, 1):
        processed_lines.append(f"{i}: {line}")
    
    return '\n'.join(processed_lines)

def main():
    print("📁 File Read & Write Challenge")
    print("=" * 30)
    
    # Ask user for filename
    filename = input("Enter filename to read: ")
    
    # Try to read the file
    content = read_file(filename)
    
    if content is None:
        print("❌ Cannot proceed without a valid file.")
        return
    
    print(f"\n📖 Original content:")
    print(content)
    
    # Process the content (add line numbers)
    processed_content = process_content(content)
    
    # Create output filename
    output_filename = f"modified_{filename}"
    
    # Write the processed content
    print(f"\n🔄 Processing and writing to '{output_filename}'...")
    
    if write_file(output_filename, processed_content):
        print(f"\n📄 Modified content written to '{output_filename}':")
        print(processed_content)
    else:
        print("❌ Failed to write the file.")

if __name__ == "__main__":
    main()