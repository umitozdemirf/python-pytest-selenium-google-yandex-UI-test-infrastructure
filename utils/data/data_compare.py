import sys


class DataCompare:
    @staticmethod
    def compare_and_merge_dict(dict1, dict2):
        same_results = list()
        sys_out = list()

        for i in dict1:
            for k in dict2:
                if k["title"] == i["title"]:
                    same_results.append(i)
                    sys_out.append(i["title"])

        sys.stdout.write(f'Same results {sys_out}\n')
        return same_results
