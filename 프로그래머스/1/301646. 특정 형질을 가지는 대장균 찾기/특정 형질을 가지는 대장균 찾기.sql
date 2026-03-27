-- 코드를 작성해주세요
# 1 -> 1번형질
# 10 -> 2번형질
# 100 -> 3번형질
# 1000 -> 4번형질
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE ((GENOTYPE & 1) > 0 OR (GENOTYPE & 4) > 0) AND ((GENOTYPE & 2) =0)
