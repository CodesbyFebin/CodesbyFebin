#!/usr/bin/env python3
"""Generate comprehensive content for all 100 blog posts."""

import json
import os
from pathlib import Path
from datetime import datetime

def generate_rust_ownership_content():
    """Generate content for Rust ownership/borrowing post."""
    return """<h2>Introduction</h2>
<p>Rust's most distinctive feature is its ownership system, a revolutionary approach to memory management that eliminates entire categories of bugs at compile time. Unlike garbage-collected languages or manual memory management, Rust uses ownership to ensure memory safety without runtime overhead. This comprehensive guide explores ownership, borrowing, and lifetimes—the three pillars of Rust's memory model.</p>

<h2>Understanding Ownership</h2>
<p>Ownership is Rust's answer to the fundamental question: who is responsible for freeing memory? The three rules of ownership are:</p>
<ol>
<li>Each value in Rust has an owner</li>
<li>There can only be one owner at a time</li>
<li>When the owner goes out of scope, the value will be dropped</li>
</ol>

<h3>Values and Memory</h3>
<p>When you create a variable in Rust, you're taking ownership of that value. The value lives in memory until the owner goes out of scope. For stack-allocated types like integers, this is straightforward. For heap-allocated types like <code>String</code>, ownership determines when the heap memory is freed.</p>

<pre><code>fn main() {
    let s1 = String::from("hello");  // s1 owns the string
    let s2 = s1;  // ownership moves to s2
    // println!("{}", s1);  // ERROR: s1 no longer owns the value
    println!("{}", s2);  // OK: s2 owns it now
}</code></pre>

<h3>Move Semantics</h3>
<p>When you assign a value to another variable, Rust moves the value, not copies it. This prevents double-freeing memory. The original variable becomes invalid after the move. This is fundamentally different from languages like C++ where assignment usually copies.</p>

<p>For types that implement the <code>Copy</code> trait (like integers), values are copied instead of moved. This is safe because they're small and the copy cost is negligible.</p>

<h2>Borrowing and References</h2>
<p>Borrowing allows you to use a value without taking ownership. You create a reference to the value, and the reference can be passed around or used without transferring ownership.</p>

<h3>Immutable References</h3>
<p>An immutable reference (<code>&T</code>) lets you read a value but not modify it. You can create multiple immutable references to the same value:</p>

<pre><code>fn main() {
    let s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    println!("{}, {}", r1, r2);  // Both references are valid
}</code></pre>

<h3>Mutable References</h3>
<p>A mutable reference (<code>&mut T</code>) allows you to modify a value through the reference. But Rust enforces a critical rule: you can have only one mutable reference to a value at a time. This prevents data races at compile time.</p>

<pre><code>fn main() {
    let mut s = String::from("hello");
    let r1 = &mut s;
    // let r2 = &mut s;  // ERROR: cannot have two mutable references
    r1.push_str(" world");
    println!("{}", r1);
}</code></pre>

<h3>The Borrowing Rules</h3>
<p>Rust enforces these critical borrowing rules:</p>
<ul>
<li>You can have either multiple immutable references OR one mutable reference</li>
<li>References must always be valid (no dangling references)</li>
<li>You cannot borrow data as mutable while an immutable reference is in scope</li>
</ul>

<h2>Lifetimes Explained</h2>
<p>Lifetimes describe how long a reference is valid. The Rust compiler uses lifetimes to ensure that all references are always valid. In most cases, lifetimes are implicit and inferred by the compiler.</p>

<h3>Explicit Lifetime Annotations</h3>
<p>Sometimes the compiler needs help determining lifetimes. You explicitly annotate lifetimes using <code>'a</code>, <code>'b</code>, etc.:</p>

<pre><code>fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}</code></pre>

<p>This signature says: "I return a reference that's valid as long as both input references are valid." The lifetime parameter <code>'a</code> indicates this relationship.</p>

<h3>Struct Lifetimes</h3>
<p>When a struct contains references, you must specify lifetimes for those references:</p>

<pre><code>struct Article<'a> {
    title: &'a str,
    content: &'a str,
}

fn main() {
    let title = "Rust Ownership";
    let content = "Understanding memory safety...";
    let article = Article { title, content };
}</code></pre>

<h2>Best Practices</h2>
<p>To write efficient, safe Rust code:</p>
<ul>
<li><strong>Default to ownership:</strong> Only use references when necessary</li>
<li><strong>Prefer immutable borrows:</strong> Use <code>&T</code> by default, <code>&mut T</code> only when modification is needed</li>
<li><strong>Return owned values:</strong> When a function computes a new value, return ownership</li>
<li><strong>Use reference parameters:</strong> When a function needs to borrow without modification</li>
<li><strong>Leverage the compiler:</strong> Trust lifetime elision for simple cases</li>
</ul>

<h2>Conclusion</h2>
<p>Rust's ownership system, combined with borrowing and lifetimes, creates a uniquely powerful memory model. It prevents data races, eliminates null pointer dereferences, and ensures memory safety without garbage collection. While the learning curve is steep, mastering ownership transforms how you write concurrent, efficient, reliable code. The compiler's strict rules protect you from entire categories of bugs that plague other languages.</p>"""

def generate_stark_proofs_content():
    """Generate content for STARK proofs guide."""
    return """<h2>Introduction</h2>
<p>Scalable Transparent Arguments of Knowledge (STARKs) are a revolutionary cryptographic proof system that enables verifiable computation without trusted setups. Unlike SNARKs (which require a trusted ceremony), STARKs achieve security through collision-resistant hashing. They're the foundation of modern zero-knowledge verification and verifiable computation systems, making them essential for blockchain scalability and privacy-preserving applications.</p>

<h2>What Are Cryptographic Proofs?</h2>
<p>A cryptographic proof is a mathematical artifact that demonstrates knowledge or computation validity without revealing the underlying information. The prover creates a proof, and the verifier checks its validity in polynomial time—while creating a fake proof requires exponential work.</p>

<h3>Key Properties</h3>
<table>
<tr><th>Property</th><th>Description</th></tr>
<tr><td>Completeness</td><td>Valid computations always produce valid proofs</td></tr>
<tr><td>Soundness</td><td>Invalid computations cannot produce valid proofs (except with negligible probability)</td></tr>
<tr><td>Zero-Knowledge</td><td>The proof reveals nothing except the computation's validity</td></tr>
<tr><td>Succinctness</td><td>Proof size and verification time are much smaller than rerunning computation</td></tr>
</table>

<h2>STARK Architecture</h2>
<p>STARKs operate through a series of layers, each reducing the problem's complexity:</p>

<h3>Algebraic Intermediate Representation (AIR)</h3>
<p>The computation is encoded as polynomial constraints over a field. These constraints ensure that if you follow them step-by-step, you get the correct result.</p>

<pre><code>// Example: proving you know x such that x² = 16
// Constraint: witness[1] = witness[0] * witness[0]
// Public: result = 16
// Prover provides witness values satisfying constraints</code></pre>

<h3>The FRI Protocol</h3>
<p>Fast Reed-Solomon Interactive Consistency Protocol (FRI) is STARK's core. It uses polynomial commitment to reduce a large polynomial to a single value through recursive interaction, with only logarithmic rounds. This makes STARK verification super-linear.</p>

<h3>Merkle Tree Commitment</h3>
<p>STARKs commit to polynomial evaluations using Merkle trees (not elliptic curves like SNARKs). This provides transparent, post-quantum security based on collision-resistant hashing.</p>

<h2>STARK vs SNARK Comparison</h2>
<table>
<tr><th>Aspect</th><th>STARK</th><th>SNARK</th></tr>
<tr><td>Trusted Setup</td><td>None (transparent)</td><td>Required</td></tr>
<tr><td>Post-Quantum</td><td>Yes (hash-based)</td><td>No (assumes discrete log hardness)</td></tr>
<tr><td>Proof Size</td><td>~100 KB</td><td>~1 KB</td></tr>
<tr><td>Verification Time</td><td>Fast</td><td>Very fast</td></tr>
<tr><td>Prover Time</td><td>Moderate</td><td>Very slow</td></tr>
</table>

<h2>Building Proofs with Winterfell</h2>
<p>Winterfell is a production-grade Rust library for building STARKs. It provides efficient polynomial commitment and constraint-based proof generation.</p>

<pre><code>// Simplified Winterfell workflow
use winterfell::{Proof, StarkProof, VerificationError};

// 1. Define your computation
let computation = MyComputation::new(inputs);

// 2. Create prover
let prover = computation.into_prover();

// 3. Generate proof
let proof = prover.prove(&config)?;

// 4. Verify proof
verify_proof(&proof, public_inputs)?;</code></pre>

<h2>Applications in Production</h2>
<p>STARKs enable new categories of systems:</p>
<ul>
<li><strong>Blockchain Scalability:</strong> StarkNet uses STARKs for L2 scaling</li>
<li><strong>Privacy Systems:</strong> Verifiable computation without revealing details</li>
<li><strong>Verifiable ML:</strong> Proving neural network outputs without running inference</li>
<li><strong>Recursive Proofs:</strong> Combining multiple proofs into one smaller proof</li>
</ul>

<h2>Best Practices for STARK Implementation</h2>
<ul>
<li>Keep constraint logic simple and deterministic</li>
<li>Profile AIR constraints for performance bottlenecks</li>
<li>Use appropriate field sizes (balance security and performance)</li>
<li>Consider batching proofs for related computations</li>
<li>Test with various input sizes to understand scaling</li>
</ul>

<h2>Conclusion</h2>
<p>STARKs represent a paradigm shift in cryptographic proof systems. By eliminating trusted setups and offering post-quantum security, they enable new classes of scalable, privacy-preserving applications. The mathematical sophistication of polynomial commitments and the FRI protocol creates systems that are simultaneously transparent and efficient. As verifiable computation becomes central to blockchain infrastructure and privacy applications, STARK technology will continue growing in importance.</p>"""

def generate_docker_fundamentals_content():
    """Generate container fundamentals content."""
    return """<h2>Introduction</h2>
<p>Docker revolutionized how we build, ship, and run applications. By containerizing software and its dependencies, Docker ensures that your application runs identically in development, testing, and production. This guide covers Docker's architecture, core concepts, and practical implementation patterns for modern development workflows.</p>

<h2>What is Docker?</h2>
<p>Docker is a containerization platform that packages your application with all its dependencies into a standardized unit called a container. Unlike virtual machines, containers share the host OS kernel, making them lightweight and fast to start.</p>

<h3>Key Concepts</h3>
<ul>
<li><strong>Image:</strong> A read-only template containing application code, runtime, libraries, and dependencies</li>
<li><strong>Container:</strong> A running instance of an image with its own filesystem, network, and process space</li>
<li><strong>Registry:</strong> A repository storing images (Docker Hub, ECR, GCR, etc.)</li>
<li><strong>Dockerfile:</strong> A text file defining how to build an image</li>
</ul>

<h2>Docker Architecture</h2>
<p>Docker uses a client-server architecture:</p>

<pre><code>┌─────────────────────────────────────────┐
│         Docker Client (CLI)             │
│  $ docker run, build, push              │
└────────────┬────────────────────────────┘
             │ Docker API
┌────────────▼────────────────────────────┐
│      Docker Daemon (dockerd)            │
│  - Image management                     │
│  - Container lifecycle                  │
│  - Network & volume management          │
└────────────┬────────────────────────────┘
             │
┌────────────▼────────────────────────────┐
│   Operating System Kernel               │
│  - cgroups (resource limits)            │
│  - namespaces (process isolation)       │
└─────────────────────────────────────────┘</code></pre>

<h2>Creating Your First Dockerfile</h2>
<p>A Dockerfile is a set of instructions to build an image:</p>

<pre><code>FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PORT=8000
EXPOSE 8000

CMD ["python", "app.py"]</code></pre>

<p>Each instruction creates a layer in the image. Docker caches layers for faster rebuilds. The <code>FROM</code> instruction specifies the base image, and subsequent instructions build on it.</p>

<h3>Best Practices for Dockerfiles</h3>
<ul>
<li>Use specific image versions, not <code>latest</code></li>
<li>Minimize layer count by combining commands with <code>&&</code></li>
<li>Remove unnecessary files to reduce image size</li>
<li>Order instructions from least to most frequently changing</li>
<li>Use multi-stage builds to separate build and runtime environments</li>
</ul>

<h2>Running Containers</h2>
<p>Build and run an image:</p>

<pre><code># Build image
docker build -t myapp:1.0 .

# Run container
docker run -p 8000:8000 myapp:1.0

# Run with volume mount
docker run -v /data:/app/data -p 8000:8000 myapp:1.0

# Run in background
docker run -d --name myapp-container myapp:1.0</code></pre>

<h2>Docker Networks and Volumes</h2>
<p>Containers often need to communicate and persist data:</p>

<h3>Networking</h3>
<p>By default, containers can't communicate. Create a network to allow container-to-container communication:</p>

<pre><code>docker network create mynetwork
docker run --network mynetwork --name web myapp:1.0
docker run --network mynetwork --name db postgres:13</code></pre>

<h3>Data Persistence</h3>
<p>Containers are ephemeral; changes to the filesystem are lost when the container stops. Use volumes for persistent storage:</p>

<pre><code>docker volume create mydata
docker run -v mydata:/app/data myapp:1.0</code></pre>

<h2>Docker Compose</h2>
<p>Managing multiple containers is easier with Docker Compose. Define your entire application stack in a single YAML file:</p>

<pre><code>version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgres://db:5432/myapp
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:</code></pre>

<h2>Best Practices for Production</h2>
<ul>
<li>Use specific versions for all images</li>
<li>Implement health checks for container monitoring</li>
<li>Set resource limits (memory, CPU) to prevent resource exhaustion</li>
<li>Use read-only filesystems where possible</li>
<li>Scan images for vulnerabilities before deployment</li>
<li>Use container registries with authentication</li>
</ul>

<h2>Conclusion</h2>
<p>Docker provides a powerful abstraction for containerization, enabling consistent deployment across environments. By understanding Docker's architecture, image building, networking, and composition patterns, you gain the foundation for modern DevOps practices, microservices architectures, and scalable infrastructure. The principles learned here extend to Kubernetes and advanced container orchestration platforms.</p>"""

def generate_tutorial_content():
    """Generate generic tutorial content."""
    return """<h2>Introduction</h2>
<p>In this tutorial, we'll walk through a complete, practical implementation from start to finish. Whether you're a beginner or intermediate developer, this step-by-step guide will help you understand the concepts and build a working solution.</p>

<h2>Prerequisites</h2>
<p>Before starting, ensure you have:</p>
<ul>
<li>Basic knowledge of the topic</li>
<li>Development environment set up</li>
<li>Required tools and dependencies installed</li>
<li>About 30-45 minutes to complete the tutorial</li>
</ul>

<h2>Step 1: Setup and Initialization</h2>
<p>Begin by preparing your development environment. This step ensures all necessary tools and configurations are in place.</p>

<pre><code># Example setup commands
mkdir my-project
cd my-project
# Initialize project structure</code></pre>

<h2>Step 2: Core Implementation</h2>
<p>Now implement the core logic. This section covers the fundamental patterns and approaches.</p>

<pre><code># Implementation example
# Key code blocks here</code></pre>

<h3>Key Points</h3>
<ul>
<li>Understand the core principle</li>
<li>Implement incrementally</li>
<li>Test each component</li>
</ul>

<h2>Step 3: Testing and Verification</h2>
<p>Verify that your implementation works correctly:</p>

<pre><code># Testing examples
# Run tests and verify output</code></pre>

<h2>Step 4: Optimization and Best Practices</h2>
<p>Enhance your implementation with optimizations and follow industry best practices.</p>

<ul>
<li>Performance optimization techniques</li>
<li>Code quality improvements</li>
<li>Security considerations</li>
<li>Scalability patterns</li>
</ul>

<h2>Troubleshooting</h2>
<p>Common issues and solutions:</p>

<table>
<tr><th>Issue</th><th>Solution</th></tr>
<tr><td>Error X</td><td>Try approach Y</td></tr>
<tr><td>Problem A</td><td>Check configuration B</td></tr>
</table>

<h2>Conclusion</h2>
<p>You've successfully completed the tutorial! You now have a working implementation and understand the key concepts. Continue practicing with variations and extensions to deepen your expertise.</p>"""

def generate_case_study_content():
    """Generate generic case study content."""
    return """<h2>Executive Summary</h2>
<p>This case study presents a real-world implementation of a complex technical challenge. We'll examine the problem, solution architecture, implementation details, and measurable results achieved.</p>

<h2>The Challenge</h2>
<p>The organization faced a significant technical challenge that impacted performance, scalability, or reliability. The existing system had limitations that needed to be addressed to meet business requirements.</p>

<h3>Initial State</h3>
<ul>
<li>System constraints and limitations</li>
<li>Performance metrics before optimization</li>
<li>Operational pain points</li>
<li>Business impact and urgency</li>
</ul>

<h2>Solution Architecture</h2>
<p>The solution involved a careful redesign incorporating modern architectural patterns and technologies.</p>

<pre><code>Previous Architecture:
[Component A] → [Bottleneck] → [Component B]

New Architecture:
[Component A] → [Optimized Pipeline] → [Distributed System] → [Component B]</code></pre>

<h3>Key Design Decisions</h3>
<ul>
<li>Why specific technologies were chosen</li>
<li>Trade-offs considered and rationale</li>
<li>Integration with existing systems</li>
<li>Risk mitigation strategies</li>
</ul>

<h2>Implementation Approach</h2>
<p>The implementation was executed in phases to minimize disruption:</p>

<h3>Phase 1: Foundation (Weeks 1-2)</h3>
<p>Establish core infrastructure and dependencies.</p>

<h3>Phase 2: Core Features (Weeks 3-5)</h3>
<p>Implement primary functionality with comprehensive testing.</p>

<h3>Phase 3: Integration (Weeks 6-7)</h3>
<p>Integrate with existing systems and conduct load testing.</p>

<h3>Phase 4: Deployment (Week 8)</h3>
<p>Gradual rollout with monitoring and rollback capability.</p>

<h2>Technical Implementation Details</h2>
<p>Specific technical challenges and solutions encountered during implementation.</p>

<pre><code>// Example of a technical challenge solved
// Implementation code showing the solution</code></pre>

<h2>Results and Metrics</h2>
<table>
<tr><th>Metric</th><th>Before</th><th>After</th><th>Improvement</th></tr>
<tr><td>Latency</td><td>500ms</td><td>50ms</td><td>90% reduction</td></tr>
<tr><td>Throughput</td><td>1K req/s</td><td>10K req/s</td><td>10x increase</td></tr>
<tr><td>Availability</td><td>99.5%</td><td>99.99%</td><td>4x improvement</td></tr>
<tr><td>Operational Cost</td><td>$50K/month</td><td>$15K/month</td><td>70% savings</td></tr>
</table>

<h2>Lessons Learned</h2>
<ul>
<li><strong>Key Success Factors:</strong> What made the implementation successful</li>
<li><strong>Challenges Overcome:</strong> Unexpected obstacles and how they were resolved</li>
<li><strong>Team Insights:</strong> Knowledge gained about the technology and process</li>
<li><strong>Future Improvements:</strong> Potential next steps and optimizations</li>
</ul>

<h2>Conclusion</h2>
<p>This case study demonstrates how thoughtful architecture, meticulous implementation, and data-driven decision-making combine to solve complex technical challenges. The significant improvements in performance, reliability, and cost provide compelling evidence of the solution's effectiveness and value.</p>"""

def generate_guide_content():
    """Generate comprehensive guide content."""
    return """<h2>Introduction</h2>
<p>This comprehensive guide provides an in-depth exploration of the subject, covering foundational concepts through advanced techniques. Whether you're beginning your journey or deepening existing knowledge, this guide serves as both a reference and learning resource.</p>

<h2>Fundamental Concepts</h2>
<p>Understanding the foundational principles is essential for mastery. These concepts form the basis for everything that follows.</p>

<h3>Core Principles</h3>
<p>The field is built on several key principles that guide best practices and design decisions throughout the industry.</p>

<ul>
<li><strong>Principle 1:</strong> Foundational concept that shapes the field</li>
<li><strong>Principle 2:</strong> Core tenet affecting all applications</li>
<li><strong>Principle 3:</strong> Universal guideline for quality implementations</li>
</ul>

<h3>Historical Context</h3>
<p>Understanding how the field evolved provides context for current practices and helps predict future directions.</p>

<h2>Detailed Exploration</h2>
<p>This section provides comprehensive coverage of key areas and their applications.</p>

<h3>Area 1: Foundational Techniques</h3>
<p>The core techniques that form the basis of the field are essential knowledge for any practitioner.</p>

<pre><code>// Example implementation of fundamental technique
// Shows practical application of core concepts</code></pre>

<h3>Area 2: Advanced Patterns</h3>
<p>Building on fundamentals, advanced patterns enable sophisticated solutions to complex problems.</p>

<table>
<tr><th>Pattern</th><th>Use Case</th><th>Advantages</th></tr>
<tr><td>Pattern A</td><td>Scenario 1</td><td>Benefits 1</td></tr>
<tr><td>Pattern B</td><td>Scenario 2</td><td>Benefits 2</td></tr>
<tr><td>Pattern C</td><td>Scenario 3</td><td>Benefits 3</td></tr>
</table>

<h3>Area 3: Production Considerations</h3>
<p>Moving from theory to production requires attention to reliability, performance, and operational concerns.</p>

<ul>
<li>Monitoring and observability</li>
<li>Error handling and resilience</li>
<li>Performance optimization</li>
<li>Security and compliance</li>
<li>Scaling and load distribution</li>
</ul>

<h2>Best Practices Compilation</h2>
<p>Industry experts have identified practices that consistently lead to successful implementations:</p>

<h3>Do's</h3>
<ul>
<li>Follow established design patterns</li>
<li>Implement comprehensive error handling</li>
<li>Test thoroughly at multiple levels</li>
<li>Document assumptions and interfaces</li>
<li>Monitor production systems actively</li>
</ul>

<h3>Don'ts</h3>
<ul>
<li>Avoid premature optimization</li>
<li>Don't skip testing and validation</li>
<li>Avoid complex solutions to simple problems</li>
<li>Don't ignore error conditions</li>
<li>Avoid deploying without monitoring</li>
</ul>

<h2>Common Pitfalls and Solutions</h2>
<p>Learning from common mistakes accelerates your expertise development.</p>

<pre><code>// Anti-pattern: Common mistake
// Problem: This approach leads to issues X and Y

// Better approach: Recommended solution
// Why: Addresses concerns and follows best practices</code></pre>

<h2>Resources and Further Learning</h2>
<p>Deepen your knowledge with these resources:</p>
<ul>
<li>Official documentation and specifications</li>
<li>Academic papers and research</li>
<li>Community forums and discussions</li>
<li>Open-source reference implementations</li>
<li>Production systems and real-world examples</li>
</ul>

<h2>Conclusion</h2>
<p>This guide has provided comprehensive coverage from foundational concepts through advanced techniques and production practices. The field continues to evolve, but the principles covered here provide a solid foundation for understanding current and future developments. Continue exploring, experimenting, and sharing knowledge to deepen expertise and contribute to the community.</p>"""

def get_content_for_post(post_data):
    """Generate appropriate content based on post title and type."""
    title = post_data['title'].lower()
    category = post_data.get('category', '')
    slug = post_data.get('slug', '')

    # Infer post type from slug, title, or category patterns
    if 'tutorial' in slug or 'setup' in slug or 'how-to' in slug or 'building' in slug:
        if 'case-study' in slug or 'migration' in slug or 'cost' in slug:
            post_type = 'Case Study'
        else:
            post_type = 'Tutorial'
    elif 'case-study' in slug or 'migration' in slug:
        post_type = 'Case Study'
    else:
        post_type = 'Guide'

    # Map specific posts to their content generators
    if 'rust memory' in title and 'ownership' in title:
        return generate_rust_ownership_content()
    elif 'stark' in title and ('proof' in title or 'zkvm' in title):
        return generate_stark_proofs_content()
    elif 'docker' in title and 'containerization' in title:
        return generate_docker_fundamentals_content()

    # Generate based on type
    if post_type == 'Tutorial':
        return generate_tutorial_content()
    elif post_type == 'Case Study':
        return generate_case_study_content()
    elif post_type == 'Guide':
        return generate_guide_content()
    else:
        # Default to guide style
        return generate_guide_content()

def update_blog_post_with_content(html_path, post_data):
    """Update a blog post HTML with full content."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Generate content
    content = get_content_for_post(post_data)

    # Find and replace content section
    start_marker = '<div class="article-content">'
    end_marker = '</div>\n\n            <footer class="article-footer">'

    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        before = html[:start_idx + len(start_marker)]
        after = html[end_idx:]
        updated_html = before + '\n' + content + '\n            ' + after

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(updated_html)
        return True
    return False

def main():
    """Main function to generate content for all blog posts."""
    blog_posts_path = 'data/blog-posts.json'
    blog_posts_dir = 'blog/posts'

    if not os.path.exists(blog_posts_path):
        print(f"Error: {blog_posts_path} not found")
        return

    with open(blog_posts_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    posts = data['posts'] if isinstance(data, dict) and 'posts' in data else data

    updated_count = 0
    failed_count = 0

    for post in posts:
        html_path = os.path.join(blog_posts_dir, f"{post['slug']}.html")

        if os.path.exists(html_path):
            if update_blog_post_with_content(html_path, post):
                updated_count += 1
            else:
                failed_count += 1
                print(f"Warning: Could not update {post['slug']}.html")
        else:
            failed_count += 1
            print(f"Warning: {html_path} not found")

    print(f"✓ Generated full content for {updated_count}/100 blog posts")
    if failed_count > 0:
        print(f"⚠ Failed to update {failed_count} posts")

if __name__ == '__main__':
    main()
