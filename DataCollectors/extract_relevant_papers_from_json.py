# ============================================================================

# These functions were used to extract relevant paper ID's from a a single OAG
# json file, based on a supplied list of relevant paper ID's.
# No docstrings or comments are provided as this is a purely data-prep script.
#
# (c) Mark Berger

# ============================================================================

import orjson
import pickle
import json

def load(line):
    try:
        return orjson.loads(line)
    except:
        return None

with open("all_ids_with_collabs_and_refs.pkl", "rb") as f:
    all_ids = pickle.load(f)


with open('0.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('0_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 0.")

with open('1.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('1_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 1.")

with open('2.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('2_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 2.")

with open('3.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('3_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 3.")

with open('4.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('4_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 4.")


with open('5.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('5_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 5.")



with open('6.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('6_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 6.")



with open('7.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('7_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 7.")



with open('8.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('8_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 8.")


with open('9.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('9_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 9.")


with open('10.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('10_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 10.")


with open('11.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('11_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 11.")


with open('12.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('12_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 12.")

with open('13.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('13_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 13.")


with open('14.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('14_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 14.")

with open('15.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('15_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 15.")

with open('16.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('16_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 16.")


with open('17.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('17_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 17.")

with open('18.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('18_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 18.")

with open('19.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('19_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 19.")

with open('20.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('20_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 20.")

with open('21.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('21_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 21.")

with open('22.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('22_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 22.")


with open('23.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('23_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 23.")


with open('24.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('24_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 24.")


with open('25.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('25_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 25.")


with open('26.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('26_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 26.")


with open('27.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('27_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 27.")


with open('28.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('28_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 28.")


with open('29.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('29_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 29.")


with open('30.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('30_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 30.")


with open('31.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('31_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 31.")


with open('32.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('32_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 32.")


with open('33.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('33_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 33.")


with open('34.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('34_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 34.")


with open('35.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('35_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 35.")


with open('36.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('36_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 36.")


with open('37.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('37_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 37.")


with open('38.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('38_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 38.")


with open('39.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('39_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 39.")


with open('40.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('40_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 40.")


with open('41.json', 'rb') as fin:
    lines = fin.readlines()


json_lines = [ll for ll in [load(l) for l in lines] if ll]

rel_lines = [l for l in json_lines if l["id"] in all_ids]

with open('41_relevant.json', 'w') as outfile:
    json.dump(rel_lines, outfile)

print("Done with 41.")

print("Done all files!")
