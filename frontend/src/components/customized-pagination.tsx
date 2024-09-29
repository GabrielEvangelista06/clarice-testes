import {
	Pagination,
	PaginationContent,
	PaginationItem,
	PaginationLink,
	PaginationNext,
	PaginationPrevious,
} from "@/components/ui/pagination";

interface PaginationProps {
	currentPage: number;
	totalPages: number;
}

export function CustomizedPagination({
	currentPage,
	totalPages,
}: PaginationProps) {
	const getPageNumbers = () => {
		const maxPagesToShow = 3;
		let startPage = Math.max(1, currentPage - Math.floor(maxPagesToShow / 2));
		const endPage = Math.min(totalPages, startPage + maxPagesToShow - 1);

		if (endPage - startPage < maxPagesToShow - 1) {
			startPage = Math.max(1, endPage - maxPagesToShow + 1);
		}

		return Array.from(
			{ length: endPage - startPage + 1 },
			(_, i) => startPage + i,
		);
	};

	const pageNumbers = getPageNumbers();

	return (
		<Pagination>
			<PaginationContent>
				<PaginationItem>
					<PaginationPrevious href={`/?page=${Math.max(1, currentPage - 1)}`} />
				</PaginationItem>

				{pageNumbers.map((page: number) => (
					<PaginationItem
						key={page}
						className={page === currentPage ? "" : "text-muted-foreground"}
					>
						<PaginationLink href={`/?page=${page}`}>{page}</PaginationLink>
					</PaginationItem>
				))}

				<PaginationItem>
					<PaginationNext
						href={`/?page=${Math.min(totalPages, currentPage + 1)}`}
					/>
				</PaginationItem>
			</PaginationContent>
		</Pagination>
	);
}
