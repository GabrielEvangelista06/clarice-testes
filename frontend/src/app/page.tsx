import { BlogPosts } from "@/components/blog-posts";

export const dynamic = "force-dynamic";

interface PageProps {
	searchParams: { [key: string]: string | string[] | undefined };
}

export default async function Home({ searchParams }: PageProps) {
	const currentPage = Number.parseInt(searchParams.page as string) || 1;
	const limit = 5;

	const res = await fetch("https://jsonplaceholder.typicode.com/posts", {
		cache: "no-store",
	});
	const allPosts = await res.json();

	const totalPages = Math.ceil(allPosts.length / limit);
	const start = (currentPage - 1) * limit;
	const end = start + limit;
	const posts = allPosts.slice(start, end);

	return (
		<BlogPosts
			allPosts={allPosts}
			posts={posts}
			currentPage={currentPage}
			totalPages={totalPages}
		/>
	);
}
