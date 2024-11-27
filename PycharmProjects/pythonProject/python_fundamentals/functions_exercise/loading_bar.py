def loading_bar(progress_number: int) -> str:
    if progress_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    percents = progress_number // 10
    dots = 10 - percents
    return f"{progress_number}% [{'%' * percents}{'.' * dots}]\nStill loading..."

number = int(input())
print(loading_bar(number))
