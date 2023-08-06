from django.utils.safestring import mark_safe


class Pagination(object):
    """
    Build reusable pagination class
    """

    def __init__(self, request, queryset, page_size=8, page_param='page', plus=5):
        """
        :param request: The requested object
        :param page_size: The amount of data displayed per page
        :param page_param: The page parameters
        :param plus: The number of pages is moved back or moved forward from current page
        """

        page = request.GET.get(page_param, '1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page

        # Calcualte the first and the last data on current page

        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size

        # Obtain the total page by using total number of data divided by the amount of data
        # displayed per page. If there is a remainder, then total page +1 for showing all 
        # data to user. 

        self.page_queryset = queryset[self.start:self.end]
        total_count = queryset.count()
        total_page_count, remainder = divmod(total_count, page_size)
        if remainder:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):

        # Get the first 5 pages and the last 5 pages of current page

        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count

        # When the total amount of pages is greater than 11, but the current page is 
        # less than 5, the start page is 1.

        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1

        # When the total amount of pages is greater than 11 and  the current page + 5 is 
        # greater than total amount of pages , the end page is number of total pages.

            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
    
        page_str_list = []
        
        if self.page > 1:
            prev = f'<li><a href="?page={self.page - 1}" aria-label="Previous"><span aria-hidden="true" class="prev"><</span></a></li>'
        else:
            prev = f'<li><a href="?page={1}" aria-label="Previous"><span aria-hidden="true"><</span></a></li>'
        
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                
                ele = f'<li class="active"><a href="?page={i}"> {i} </a></li>'
            else:

                ele = f'<li><a href="?page={i}"> {i} </a></li>'
            page_str_list.append(ele)

        if self.page < self.total_page_count:
            prev = f'<li><a href="?page={self.page + 1}" aria-label="Next"><span aria-hidden="true">></span></a></li>'
        else:
            prev = f'<li><a href="?page={self.total_page_count}" aria-label="Next"><span aria-hidden="true">></span></a></li>'
        
        page_str_list.append(prev)

        search_string = """
        <li>
            <form class="search-form" method="get">
                <input type="text" name="page" class="form-control search-input" placeholder="Page" >
                <button class="btn btn-default search-btn" type="submit">Go!</button>
            </form>
        <li>
        """

        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string