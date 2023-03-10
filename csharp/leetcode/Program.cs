namespace LeetCode
{
    class Program
    {
        static void Main(string[] args)
        {
            var s = new Solution();
            var p = "Bob hit a ball, the hit BALL flew far after it was hit.";
            var b = new string[] {"hit"};
            var r = s.MostCommonWord(p, b);
            System.Console.WriteLine(r);
        }
    }
}