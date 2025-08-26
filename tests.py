from functions.get_files_info import get_files_info


test1 = get_files_info("calculator", ".")
print("Results for current directory:")
print(test1)

test2 = get_files_info("calculator", "pkg")
print("Results for 'pkg' directory:")
print(test2)

test3 = get_files_info("calculator", "/bin")
print("Results for '/bin' directory:")
print(test3)

test4 = get_files_info("calculator", "../")
print("Results for '../' directory:")
print(test4)