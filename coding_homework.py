def clean_text(file):
    fp1 = open(file, "r")
    fp2 = open("book_new","w")
    punct = ".,;:!?-()*|'´@/[]{}_<>+-"
    for letter in fp1:
        for p in punct:
            letter = letter.replace(p, " ")
        fp2.write(letter)
    fp1.close()
    fp2.close()

def create_list ():
    fp2 = open("book_new", "r")
    list1 = []
    list2 = []

    for letter in fp2:
        list1.append(letter)
        list1 = letter.split()
        list2 += list1

    list_clean = []
    for i in list2:
        i = i.lower()
        if i not in list_clean:
            list_clean.append(i)
    return len(list_clean)

clean_text("Alice_in_Wonderland")
long1 = create_list()

clean_text("Harry_Potter")
long2 = create_list()

clean_text("The_Lord_Of_The_Rings")
long3 = create_list()

print("Alice_in_Wonderland","=", long1)
print("Harry_Potter","=", long2)
print("The_Lord_Of_The_Rings","=", long3)

if max(long1,long2,long3) == long1:
    print("Result: Alice_in_Wonderland is the book with more distinct words (",long1,")")
if max(long1, long2, long3) == long2:
    print("Result: Harry_Potter is the book with more distinct words (",long2,")")
if max(long1, long2, long3) == long3:
    print("Result: The_Lord_Of_The_Rings is the book with more distinct words (",long3,")")