"""
Created on Sat Jan 20 13:29:49 2024

@author: Xenia Skorodelova
"""

#%% функция для подсчета статистических критериев по отдельности
# виды тестов test 
# scist.shapiro = sh
# scist.bartlett = b
# Для равных дисперсий (p-val bartlett > 0.05)
# scist.ttest_ind = ttest_ind - независимые
# scist.ttest_rel = ttest_rel - зависимые
# Если дисперсии не равны (p-val bartlett < 0.05)
# scist.ttest_ind = ttest_ind_eqF - независимые
# scist.ttest_rel = ttest_rel_eqF - зависимые
# Для маленьких выборок и ненормального распределения
# scist.mannwhitneyu = m
# scist.wilcoxon = w
def stat_calculation (seq1, seq2, test):
    #импорт библиотеки со стат. методами
    import scipy.stats as scist
    #Тест Шапиро на нормальность распределения
    if test == 'sh':
        norm1 = scist.shapiro(seq1)[1] 
        norm2 = scist.shapiro(seq2)[1]
        if norm1 > 0.05 and norm2 > 0.05: 
            print(f'Распределения нормальные \np-value shapiro seq1: {norm1} seq2: {norm2}')
        else: 
            print(f'Распределения НЕнормальные \np-value shapiro seq1: {norm1} seq2: {norm2}')    
    #Тест Бартлетта на равность дисперсий
    if test == 'b':
        bart = scist.bartlett(seq1, seq2)[1]
        print(f'дисперсии примерно равны p-value - {bart}')
    #t-критерий Стьюдента для зависимых выборок и равных дисперсий
    if test == 'ttest_rel':
        print('Метод t-критерий Стьюдента для зависимых выборок и равных дисперсий') 
        print('two - sided p-value = ', scist.ttest_rel(seq1, seq2)[1], 
              '\nless p-value = ', scist.ttest_rel(seq1, seq2, alternative='less')[1], 
              '\ngreater p-value = ', scist.ttest_rel(seq1, seq2, alternative='greater')[1])
    #t-критерий Стьюдента для НЕзависимых выборок и равных дисперсий
    if test == 'ttest_ind':
        print('Метод t-критерий Стьюдента для НЕзависимых выборок и равных дисперсий') 
        print('two - sided p-value = ', scist.ttest_ind(seq1, seq2)[1], 
              '\nless p-value = ', scist.ttest_ind(seq1, seq2, alternative='less')[1], 
              '\ngreater p-value = ', scist.ttest_ind(seq1, seq2, alternative='greater')[1])
    #t-критерий Стьюдента для зависимых выборок и НЕ равных дисперсий equal_var=False
    if test == 'ttest_rel_eqF':
        print('Метод t-критерий Стьюдента для зависимых выборок и НЕ равных дисперсий') 
        print('two - sided p-value = ', scist.ttest_rel(seq1, seq2, equal_var=False)[1], 
              '\nless p-value = ', scist.ttest_rel(seq1, seq2, equal_var=False, alternative='less')[1], 
              '\ngreater p-value = ', scist.ttest_rel(seq1, seq2, equal_var=False, alternative='greater')[1])
    #t-критерий Стьюдента для НЕзависимых выборок и НЕ равных дисперсий equal_var=False
    if test == 'ttest_ind_eqF':
        print('t-критерий Уэлча - Метод t-критерий Стьюдента для НЕзависимых выборок и НЕ равных дисперсий') 
        print('two - sided p-value = ', scist.ttest_ind(seq1, seq2, equal_var=False)[1], 
              '\nless p-value = ', scist.ttest_ind(seq1, seq2, equal_var=False, alternative='less')[1], 
              '\ngreater p-value = ', scist.ttest_ind(seq1, seq2, equal_var=False, alternative='greater')[1])
    #Тест Манна-Уитни
    if test == 'm':
        print('Mann-Whitneyu-test','\ntwo - sided p-value = ', scist.mannwhitneyu(seq1, seq2)[1], 
              '\nless p-value = ', scist.mannwhitneyu(seq1, seq2, alternative='less')[1], 
              '\ngreater p-value = ',scist.mannwhitneyu(seq1, seq2, alternative='greater')[1]) 
    #Тест Уилкоксона 
    if test == 'w':
        print('Wilcoxon-test','\ntwo - sided p-value = ', scist.wilcoxon(seq1, seq2)[1], 
              '\nless p-value = ', scist.wilcoxon(seq1, seq2, alternative='less')[1], 
              '\ngreater p-value = ',scist.wilcoxon(seq1, seq2, alternative='greater')[1])
    return

