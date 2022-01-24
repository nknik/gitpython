import re
def repeating_letter_a(text):
    result = re.search(r"[a|A].*[a|A]", text)
    return result != None

# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True
# print(re.findall(r"[^a-zA-Z .]","Arya .@")) # [^abc] string dont have abc
# print(re.findall(r"\w","Arya 123.@")) # [^abc] string dont have abc
# rr=re.match(r"(\w*).(\w*)","11111.11")
# print(rr,"",rr.groups())
# m = re.match(r"(\d+)\.(\d+)", "27.1835")
# print(m,m.groups())
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: [A-Z]{3,}"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[0].split()[1])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))