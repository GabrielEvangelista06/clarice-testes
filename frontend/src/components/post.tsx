import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";

export type Post = {
	id: number;
	title: string;
	body: string;
};

export function Post({ id, title, body }: Post) {
	return (
		<Link href={`/posts/${id}`} className="block">
			<Card>
				<CardHeader>
					<CardTitle className="scroll-m-20 text-2xl font-semibold tracking-tight">
						{title}
					</CardTitle>
				</CardHeader>
				<CardContent>
					<p className="leading-7 [&:not(:first-child)]:mt-6">
						{body.slice(0, 50)}...
					</p>
				</CardContent>
			</Card>
		</Link>
	);
}
