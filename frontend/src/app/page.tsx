import { BlogPosts } from "@/components/blog-posts";
import type { Metadata } from "next";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
	title: "Blog Posts - Clarice",
	description: "A list of blog posts.",
};

interface PageProps {
	searchParams: { [key: string]: string | string[] | undefined };
}

export default async function Home({ searchParams }: PageProps) {
	// Get the current page number from the search parameters, default to 1 if not provided
	const currentPage = Number.parseInt(searchParams.page as string) || 1;
	const limit = 5;

	// Fetch all posts from the API
	const res = await fetch("https://jsonplaceholder.typicode.com/posts", {
		cache: "no-store", // Disable caching to always fetch fresh data
	});
	const allPosts = await res.json();

	// Calculate the total number of pages
	const totalPages = Math.ceil(allPosts.length / limit);
	// Calculate the start and end indices for slicing the posts array
	const start = (currentPage - 1) * limit;
	const end = start + limit;
	// Slice the posts array to get only the posts for the current page
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
