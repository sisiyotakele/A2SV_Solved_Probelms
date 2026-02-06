class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c_p = defaultdict(list)
        for p in paths:
            paths_comp = p.split()
            dirc = paths_comp [0]

            for f_i in paths_comp[1:]:
                paren_index = f_i.find("(")

                file_name  = f_i [: paren_index]
                file_con = f_i [paren_index + 1 : - 1]

                full_path = f"{dirc}/{file_name}"
                c_p[file_con].append(full_path)
        return [file_path for file_path in c_p.values() if len(file_path) > 1]
